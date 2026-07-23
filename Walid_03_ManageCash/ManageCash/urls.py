from django.urls import path
from ManageCash.views import *


urlpatterns = [
    path('', login_view, name='login_view'),
    path('register/', register_view, name='register_view'),
    path('logout/', logout_view, name='logout_view'),

    path('dashboard/', dashboard, name='dashboard'),
    path('profile/', profile_view, name='profile'),
    path('transaction-history/', transaction_history, name='transaction_history'),

    path('add-cash/', addAddCash, name='addAddCash'),
    path('delete-cash/<str:c_id>/', deleteAddCash, name='deleteAddCash'),

    path('add-expense/', addExpense, name='addExpense'),
    path('delete-expense/<str:e_id>/', deleteExpense, name='deleteExpense'),
]