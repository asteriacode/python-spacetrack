
BASE_URL = "https://www.space-track.org"

class Query:
    def __init__(self, controller="basicspacedata", action="query"):
        self.controller = controller
        self.action = action
        self.fragments = []
        self.used_predicates = []

    # Unique predicates - Should only be used once and we raise an error if they're used twice
    def __unique(self, key, value):
        if key in self.used_predicates:
            raise Error("Used %s predicate twice" % key)

        self.used_predicates += [key]
        self.fragments += [key, value]
        return self

    # Flag predicates - SHOULD only be used once, but it's fine if they're specified twice
    def __flag(self, key, val):
        if key not in self.used_predicates:
            self.used_predicates += [key]
            self.fragments += [key, val]

        return self

    # Columns is an array of tuples, ie [("name", "asc"), ("date", "desc")]
    def order_by(self, columns):
        if "orderby" in self.used_predicates:
            raise Error("Used order_by predicate twice")

        self.used_predicates += ["order_by"]

        orderby_str = ",".join(["%s %s" % (col, order) for (col, order) in columns])
        self.fragments += ["orderby", orderby_str]
        return self

    # Column Predicate - can be used as many times as you want, but not for the same column
    def column(self, column, *values):
        return self.__unique(column, ",".join(values))

    def obj_class(self, obj_class):
        return self.__unique("class", obj_class)

    def limit(self, n, skip=0):
        return self.__unique("limit", "%s,%s" % (n, skip))
        
    def metadata(self):
        return self.__flag("metadata", "true")

    def distinct(self):
        return self.__flag("distinct", "true")

    def empty_result(self):
        return self.__flag("emptyresult", "show")

    # Other stuff
    def to_url(self):
        stub = "%s/%s/%s/" % (BASE_URL, self.controller, self.action)
        stub += "/".join(self.fragments)
        return stub