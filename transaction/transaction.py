from dataclasses import dataclass
from decimal import Decimal
from uuid import UUID


@dataclass
class Transaction:
    id_: UUID
    from_account: UUID
    to_account: UUID
    amount: Decimal
    # balance_brutto: Decimal
    # balance_netto: Decimal
    currency: str
    status: str