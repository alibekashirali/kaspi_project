"""webapp URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from webapp import views
from uuid import uuid4

urlpatterns = [
    path('', views.index),
    path('accounts/', views.accounts_list, name='accounts_url'),
    # path('customers/', views.customer_list),
    path('account/create/', views.create_account, name='account_create_url'),
    path('account/<uuid:id>/', views.transactions_list, name='account_transactions_url'),
    path('account/create_transaction/', views.create_transaction, name='create_transaction_url'),

    # path('accounts/', views.accounts_list),
    # path('transactions/', views.accounts_list),

    # path('admin/', admin.site.urls),
]
