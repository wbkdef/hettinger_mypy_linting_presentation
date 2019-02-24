"""Examples modified from the python dataclass documentation"""

from dataclasses import dataclass

@dataclass
class InventoryItemDC:
    '''Class for keeping track of an item in inventory.'''
    name: str
    unit_price: float
    quantity_on_hand: int = 0

    #  __c:  The "@dataclass" decorator supplies the
    #   __init__, and much more:

    def total_cost(self) -> float:
        return self.unit_price * self.quantity_on_hand
iidc = InventoryItemDC("IIDC", unit_price=3.2)
print(f" iidc: {iidc}")
# iidc: InventoryItemDC(name='IIDC', unit_price=3.2,
# quantity_on_hand=0)


class InventoryItem:
    '''Class for keeping track of an item in inventory.'''
    #  __c:  Note - you can now specify instance
    #   attributes and their types outside the __init__!
    name: str
    unit_price: float
    quantity_on_hand: int

    # __c The "@dataclass" class decorator supplies
    #  this entire init!
    def __init__(self, name: str, unit_price: float,
                 quantity_on_hand: int = 0):
        self.name = name
        self.unit_price = unit_price
        self.quantity_on_hand = quantity_on_hand

    def total_cost(self) -> float:
        return self.unit_price * self.quantity_on_hand
ii = InventoryItem("My II", unit_price=3.2)
print(f" ii: {ii}")
# ii: <__main__.InventoryItem object at 0x000002CF22901550>

# __c The @dataclass decorator (optionally)
#  supplies many more methods...
@dataclass(init=True, repr=True, eq=True,
           order=False, unsafe_hash=False, frozen=False)
class C:
   ...


# __c There is also a way to create
#  NamedTuples with type hints
#  (and default values)
from typing import NamedTuple
class Coordinates(NamedTuple):
    x: float
    y: float
    z: float = 0
print(Coordinates(2, y=3.5))
# Coordinates(x=2, y=3.5, z=0)