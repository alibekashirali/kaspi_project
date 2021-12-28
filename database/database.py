from abc import ABC, abstractmethod
from dataclasses import dataclass
from typing import List
from uuid import UUID

from account.account import Account
from customer.customer import Customer
from transaction.transaction import Transaction


class ObjectNotFound(ValueError):
    ...


@dataclass
class AccountDatabase(ABC):  # <---- INTERFACE

    @abstractmethod
    def save(self, account: Account) -> None:
        pass

    @abstractmethod
    def clear_all(self) -> None:
        pass

    @abstractmethod
    def get_objects(self) -> List[Account]:
        pass

    @abstractmethod
    def get_object(self, id_: UUID) -> Account:
        pass
    
    @abstractmethod
    def delete(self, account: Account) -> None:
        pass


# @dataclass
# class CustomerDatabase(ABC):  # <---- INTERFACE
    # def save(self, customer: Customer) -> None:
    #     print("I am going to save this:", customer)
    #     return self._save(customer=customer)

    # @abstractmethod
    # def _save(self, customer: Customer) -> None:
    #     pass

    # @abstractmethod
    # def clear_all(self) -> None:
    #     pass

    # @abstractmethod
    # def get_objects(self) -> List[Customer]:
    #     pass

    # @abstractmethod
    # def get_object(self, id_: UUID) -> Customer:
    #     pass
    
    # @abstractmethod
    # def delete(self, customer: Customer) -> None:
    #     pass


@dataclass
class TransactionDatabase(ABC):  # <---- INTERFACE

    @abstractmethod
    def save(self, transaction: Transaction) -> None:
        pass

    @abstractmethod
    def clear_all(self) -> None:
        pass

    @abstractmethod
    def get_objects(self) -> List[Transaction]:
        pass

    @abstractmethod
    def get_object(self, id_: UUID) -> Transaction:
        pass
    
    # @abstractmethod
    # def delete(self, transaction: Transaction) -> None:
    #     pass
