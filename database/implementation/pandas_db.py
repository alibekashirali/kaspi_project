from typing import List
from uuid import UUID, uuid4
import pandas as pd
from pandas import DataFrame
from account.account import Account
from customer.customer import Customer
from transaction.transaction import Transaction
from database.database import AccountDatabase, TransactionDatabase
from database.database import ObjectNotFound


class AccountDatabasePandas(AccountDatabase):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self._objects: DataFrame = pd.DataFrame(columns=["id", "currency", "balance", "transactions"])
        try:
            self._objects = pd.read_pickle("database.pk")
            print("Got database from disk:", self._objects)
        except:
            pass

    def clear_all(self) -> None:
        self._objects = pd.DataFrame(columns=["id", "currency", "balance", "transactions"])
        self._objects.to_pickle("database.pk")

    def save(self, account: Account) -> None:
        if account.id_ is None:
            account.id_ = uuid4()

        if account.id_ in list(self._objects["id"]):
            self._objects = self._objects[self._objects["id"] != account.id_]

        new_row = pd.DataFrame({
            "id": [account.id_],
            "currency": [account.currency],
            "balance": [account.balance],
            "transactions": [account.transactions]
        })
        self._objects = self._objects.append(new_row)
        self._objects.to_pickle("database.pk")

    def get_objects(self) -> List[Account]:
        result = []
        for index, row in self._objects.iterrows():
            result.append(Account(
                id_=row["id"],
                currency=row["currency"],
                balance=row["balance"],
                transactions=row["transactions"],
            ))
        return result

    def get_object(self, id_: UUID) -> Account:
        if id_ in list(self._objects["id"]):
            filtered = self._objects[self._objects["id"] == id_].iloc[0]
            account = Account(
                id_=filtered["id"],
                currency=filtered["currency"],
                balance=filtered["balance"],
                transactions=filtered["transactions"],
            )
            return account
        print("--------this object is not found:", id_)
        print(self._objects.info())
        raise ObjectNotFound("Pandas error: object not found")

    def delete(self, account: Account) -> None:

        if account.id_ not in list(self._objects["id"]):
            raise ObjectNotFound("Pandas error: object not found")

        # self._objects.set_index('id')
        self._objects = self._objects.drop(self._objects[(self._objects.id == str(account.id_))].index)
        self._objects.to_pickle("database.pk")
        print("Deleted from Pandas")


class TransactionDatabasePandas(TransactionDatabase):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self._objects: DataFrame = pd.DataFrame(columns=["id", "from_account", "to_account", "amount", "currency", "status"])
        try:
            self._objects = pd.read_pickle("transactions.pk")
            print("Got database from disk:", self._objects)
        except:
            pass

    def clear_all(self) -> None:
        self._objects = pd.DataFrame(columns=["id", "from_account", "to_account", "amount", "currency", "status"])
        self._objects.to_pickle("transactions.pk")

    def save(self, transaction: Transaction) -> None:
        if transaction.id_ is None:
            transaction.id_ = uuid4()

        if transaction.id_ in list(self._objects["id"]):
            self._objects = self._objects[self._objects["id"] != transaction.id_]

        new_row = pd.DataFrame({
            "id": [transaction.id_],
            "from_account": [transaction.from_account], 
            "to_account": [transaction.to_account], 
            "amount": [transaction.amount], 
            "currency": [transaction.currency], 
            "status": [transaction.status],
        })
        self._objects = self._objects.append(new_row)
        self._objects.to_pickle("transactions.pk")

    def get_objects(self) -> List[Transaction]:
        result = []
        for index, row in self._objects.iterrows():
            result.append(Transaction(
                id_ = row["id"], 
                from_account = row["from_account"], 
                to_account = row["to_account"], 
                amount = row["amount"], 
                currency = row["currency"], 
                status = row["status"])
                )
        return result

    def get_object(self, id_: UUID) -> Account:
        if id_ in list(self._objects["id"]):
            filtered = self._objects[self._objects["id"] == id_].iloc[0]
            transaction = Transaction(
                id_ = row["id"], 
                from_account = row["from_account"], 
                to_account = row["to_account"], 
                amount = row["amount"], 
                currency = row["currency"], 
                status = row["status"]
                )
            return account
        print("--------this object is not found:", id_)
        print(self._objects.info())
        raise ObjectNotFound("Pandas error: object not found")

    # def delete(self, account: Account) -> None:

    #     if account.id_ not in list(self._objects["id"]):
    #         raise ObjectNotFound("Pandas error: object not found")

    #     # self._objects.set_index('id')
    #     self._objects = self._objects.drop(self._objects[(self._objects.id == str(account.id_))].index)
    #     self._objects.to_pickle("database.pk")
    #     print("Deleted from Pandas")


