import json
from uuid import uuid4
from decimal import Decimal
from django.shortcuts import redirect


from django.http import HttpResponse, HttpRequest
from django.template.loader import get_template
import os

from django.shortcuts import render

from account.account import Account
from customer.customer import Customer
from database.database import ObjectNotFound
from database.implementation.pandas_db import AccountDatabasePandas, TransactionDatabasePandas
from test_all import PandasDBActivate

dbname: str = os.environ.get("pg_dbname", "")
if dbname == "":
    database = AccountDatabasePandas()
    print("Using Pandas")
else:
    print("Error with connection to db")



def accounts_list(request: HttpRequest) -> HttpResponse:
    # dbs = TransactionDatabasePandas()
    # transac = dbs.get_objects()
    
    accounts = database.get_objects()
    # for account in accounts:
    #     currency.append(account.currency)
    # currency = list(dict.fromkeys(currency))
    if len(accounts) == 0:
        PandasDBActivate.dbs()

    return render(request, "accounts.html", context={"accounts": accounts})

def transactions_list(request: HttpRequest, id) -> HttpResponse:
    # print(id)
    account = database.get_object(id)
    databs = TransactionDatabasePandas()
    transactions = databs.get_objects()
    # if len(transactions) == 0:
    #     PandasDBActivate.dbs()

    return render(request, "account.html", context={"transactions": transactions, "account": account})



# def customer_list(request: HttpRequest) -> HttpResponse:
#     customer = database.get_objects()
#     data = CreateCustomer().test_customer_create_with_accounts()

#     return render(request, "index.html", context={"customers": [customer1, customer2]})


# def customer_list(request: HttpRequest) -> HttpResponse:
#     customer = database.get_objects()

def index(request: HttpRequest) -> HttpResponse:
    return HttpResponse(content="""
    <html>
        <body>
           <h1>Hello, World!</h1>
           <h3>Try to access <a href="/accounts/">/accounts/</a></h3>
        </body>
    </html>
    """)


def accounts(request: HttpRequest) -> HttpResponse:
    accounts = database.get_objects()

    if request.method == "GET":
        json_obj = [account.to_json() for account in accounts]
        return HttpResponse(content=json.dumps(json_obj))

    if request.method == "POST":
        try:
            account = Account.from_json_str(request.body.decode("utf8"))
            account.id_ = uuid4()
            try:
                database.get_object(account.id_)
                return HttpResponse(content=f"Error: object already exists, use PUT to update", status=400)
            except ObjectNotFound:
                database.save(account)
                return HttpResponse(content=account.to_json_str(), status=201)
        except Exception as e:
            return HttpResponse(content=f"Error: {e}", status=400)

    if request.method == "PUT":
        try:
            account = Account.from_json_str(request.body.decode("utf8"))
            database.get_object(account.id_)
            database.save(account)
            return HttpResponse(content="OK", status=200)
        except Exception as e:
            return HttpResponse(content=f"Error: {e}", status=400)

def create_account(request):
    # PandasDBActivate.dbs()
    # database.clear_all()
    currency = request.GET['currencySelect']
    account = Account.new_account(uuid4(), currency, Decimal(0))
    database.save(account)
    return redirect('accounts_url')

def create_transaction(request: HttpRequest) -> HttpResponse:
    accounts = database.get_objects()
    # PandasDBActivate.transac()
    return render(request, "transaction.html", context={"accounts": accounts})

