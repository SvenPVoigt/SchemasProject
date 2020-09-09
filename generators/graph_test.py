from pydantic import BaseModel, Field
from typing import Optional, List

class Machine(BaseModel):
    name: str = 'The Machine'
    hasPart: 'Component' = None

class Component(BaseModel):
    name: str = 'The Component'
    isPartOf: Machine = None


if __name__ == "__main__":
    Machine.update_forward_refs()

    m = Machine()
    c = Component()

    m.hasPart = c
    c.isPartOf = m

    print(c.name, c.isPartOf.name)
    print(Machine.schema_json(indent=2))
