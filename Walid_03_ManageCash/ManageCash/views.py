from django.shortcuts import render, redirect
from ManageCash.models import *
from ManageCash.forms import *
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import login, logout
from django.contrib.auth.decorators import login_required


def register_view(request):

    form_data = userForm()

    if request.method == 'POST':
        form_data = userForm(request.POST)
        if form_data.is_valid():
            form_data.save()
            return redirect('login_view')

    context = {
        'form_data' : form_data
    }

    return render(request, 'register.html', context)


def login_view(request):

    form_data = AuthenticationForm()

    if request.method == 'POST':
        form_data = AuthenticationForm(request, data = request.POST)
        if form_data.is_valid():
            user = form_data.get_user()
            login(request, user)
            return redirect('dashboard')

    context = {
        'form_data' : form_data
    }

    return render(request, 'login.html', context)

@login_required
def logout_view(request):

    logout(request)
    return redirect('login_view')

@login_required
def dashboard(request):

    cash_history_data = AddCash.objects.filter(user=request.user)
    expense_history_data = Expense.objects.filter(user=request.user)

    total_cash_added = 0.00
    total_expense = 0.00

    for each_cash_history_data in cash_history_data:
        total_cash_added = total_cash_added + float(each_cash_history_data.amount)

    for each_expense_history_data in expense_history_data:
        total_expense = total_expense + float(each_expense_history_data.amount)

    net_amount = total_cash_added - total_expense

    context = {
        'net_amount' : net_amount,
        'total_cash_added' : total_cash_added,
        'total_expense' : total_expense
    }

    return render(request, 'dashboard.html', context)

@login_required
def profile_view(request):

    profile_data = customUser.objects.get(username = request.user.username)

    form_data = profileForm(instance=profile_data)

    context = {
        'form_data' : form_data
    }

    return render(request, 'profile.html', context)

@login_required
def addAddCash(request):

    form_data = addCashForm()

    if request.method == "POST":
        form_data_partial = addCashForm(request.POST)
        if form_data_partial.is_valid():
            form_data = form_data_partial.save(commit=False)
            form_data.user = request.user
            form_data.save()
            return redirect('dashboard')

    context = {
        'form_data' : form_data
    }

    return render(request, 'add_cash.html', context)

@login_required
def deleteAddCash(request, c_id):

    AddCash.objects.get(id = c_id).delete()
    return redirect('dashboard')



@login_required
def addExpense(request):

    form_data = expenseForm()

    if request.method == "POST":
        form_data_partial = expenseForm(request.POST)
        if form_data_partial.is_valid():
            form_data = form_data_partial.save(commit=False)
            form_data.user = request.user
            form_data.save()
            return redirect('dashboard')

    context = {
        'form_data' : form_data
    }

    return render(request, 'add_expense.html', context)

@login_required
def deleteExpense(request, e_id):

    Expense.objects.get(id = e_id).delete()
    return redirect('dashboard')


@login_required
def transaction_history(request):

    cash_history_data = AddCash.objects.filter(user=request.user)
    expense_history_data = Expense.objects.filter(user=request.user)

    context = {
        'cash_history_data' : cash_history_data,
        'expense_history_data' : expense_history_data,
    }

    return render(request, 'transactions.html', context)
