from pydantic import BaseModel
import graph_test
from inspect import isclass

for key, val in vars(graph_test).items():
    if isclass(val):
        if issubclass(val, BaseModel):
            print(key)
            val.update_forward_refs()


m = graph_test.Machine()

print(m.schema_json(indent=2))
