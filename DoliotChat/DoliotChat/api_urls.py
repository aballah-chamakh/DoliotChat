from django.urls import path
from django.conf.urls import include
from chat import urls as chat_api_url
from account import urls as account_api_url
urlspatterns = [

path('',include(chat_api_url)),
path('',include(account_api_url))
]
