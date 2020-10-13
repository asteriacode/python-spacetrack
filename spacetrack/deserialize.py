from datetime import datetime as p_datetime

class FromDict:
    def __init__(self, obj):
        for field in self.fields:
            key_name = None
            dst_name = None
            map_function = lambda x: x # Identity
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

            if key_name in obj.keys():
                self.__dict__[dst_name] = map_function(obj[key_name])

def datetime(x):
    return p_datetime.strptime(x, "%Y-%m-%dT%H:%M:%S.%f")
