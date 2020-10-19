from datetime import datetime as p_datetime


class FromDict:
    def __init__(self, obj):
        for field in self.fields:
            key_name = None
            dst_name = None
            map_function = self.__identity
            if isinstance(field, str):
                key_name = field
                dst_name = key_name
            else:
                key_name = field[0]
                if len(field) > 1:
                    dst_name = field[1]
                else:
                    dst_name = key_name

                if len(field) > 2:
                    map_function = field[2]

            if key_name in obj.keys() and obj[key_name] is not None:
                self.__dict__[dst_name] = map_function(obj[key_name])

    def __identity(x):
        return x


def datetime(x):
    return p_datetime.strptime(x, "%Y-%m-%dT%H:%M:%S.%f")


def boolean(x):
    return x.lower() == "y"
