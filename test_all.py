from decimal import Decimal
from uuid import uuid4

from account.account import Account
from customer.customer import Customer
from transaction.transaction import Transaction
from database.implementation.pandas_db import AccountDatabasePandas, TransactionDatabasePandas
from database.database import AccountDatabase, TransactionDatabase

class CreateCustomer:
    def test_customer_create(self) -> None:
        customer1_id = uuid4()
        customer2_id = uuid4()
        customer = Customer(
            id_=customer1_id,
            first_name="Timur",
            last_name="Bakibayev",
            age=39,
            accounts=[],
        )

        customer2 = Customer(
            id_=customer2_id,
            first_name="Alibek",
            last_name="Ashirali",
            age=25,
            accounts=[],
        )


    def test_customer_create_with_accounts(self) -> None:
        customer1_id = uuid4()
        customer2_id = uuid4()
        customer = Customer(
            id_=customer1_id,
            first_name="Timur",
            last_name="Bakibayev",
            age=39,
            accounts=[],
        )

        customer2 = Customer(
            id_=customer2_id,
            first_name="Alibek",
            last_name="Ashirali",
            age=25,
            accounts=[],
        )

        account1_id = uuid4()
        account2_id = uuid4()
        account1 = Account(
            id_=account1_id,
            # customer_id=customer1_id,
            currency="KZT",
            balance=Decimal(1000),
        )
        account2 = Account(
            id_=account2_id,
            # customer_id=customer1_id,
            currency="USD",
            balance=Decimal(500),
        )



class PandasDBActivate:
    def dbs() -> None:
        implementation = AccountDatabasePandas
        database = implementation()

        # database.clear_all()
        account = Account.random()
        database.save(account)
        # got_account = database.get_object(account.id_)
  
        # database.delete(account)
        # print("Here is deleted")

    # def create_account(database: AccountDatabasePandas) -> None:
    #     account1 = Account.random()
    #     database.save(account1)

    def transac() -> None:
        implementation = AccountDatabasePandas
        database = implementation()
        accounts = database.get_objects()
        # print(accounts[0].id_, accounts[1].id_)

        transaction = Transaction(
            id_=uuid4(), 
            from_account = accounts[0].id_, 
            to_account = accounts[1].id_, 
            amount = Decimal(200), 
            currency = "KZT", 
            status = "OK"
        )

        dbs = TransactionDatabasePandas()
        dbs.save(transaction)
        print(dbs.get_objects())



