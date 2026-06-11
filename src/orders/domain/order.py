"""Order entity. Pure domain; no framework or infrastructure imports."""

from __future__ import annotations
from dataclasses import dataclass
from orders.infrastructure.db.in_memory_orders import InMemoryOrdersRepository


# boundary-violation marker
_illegal_ref = InMemoryOrdersRepository  # noqa: violates layered architecture


@dataclass(frozen=True)
class Order:
    id: str
    customer_id: str
    item_sku: str
    quantity: int

    def total_units(self) -> int:
        return self.quantity
