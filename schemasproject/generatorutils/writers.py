from typing import Dict, Tuple, Optional

# Reversed the field_class_to_schema map taken from https://github.com/samuelcolvin/pydantic/blob/master/pydantic/schema.py to get below map

# Tuple keys are (json type, json format, uniqueItems)
# values are python types
json_schema_to_field_class: dict[Tuple[str, Optional[str], Optional[bool]], str] = {
    ('string'): 'str',
    ('string', 'path'): 'Path',
    ('string', 'date-time'): 'datetime',
    ('string', 'date'): 'date',
    ('string', 'time'): 'time',
    ('number', 'time-delta'): 'timedelta',
    ('string', 'ipv4network'): 'IPv4Network',
    ('string', 'ipv6network'): 'IPv6Network',
    ('string', 'ipv4interface'): 'IPv4Interface',
    ('string', 'ipv6interface'): 'IPv6Interface',
    ('string', 'ipv4'): 'IPv4Address',
    ('string', 'ipv6'): 'IPv6Address',
    ('string', 'binary'): 'bytes',
    ('boolean'): 'bool',
    ('integer'): 'int',
    ('number'): 'float',
    ('string', 'uuid'): 'UUID',
    ('object'): 'Dict',
    ('array'): 'List',
    ('array', False): 'List',
    ('array', True): 'Set'
}


base_class = '''\n
class {}(BaseModel):
    """
    {}
    """
    {}
'''


class PydanticWriter:
    def __init__(self, path, type_mapper=lambda x: x):
        with open(path, 'w+') as f:
            f.write('\n'.join([
                'from pydantic import BaseModel, Field, AnyHttpUrl',
                'from uuid import UUID',
                'from typing import Union, Dict, List, Set, Optional',
                'from datetime import date, datetime, time, timedelta'
            ]))

        self.path = path
        self.type_mapper = type_mapper

    def add_class(self, name, description, dictionary of attributes):
