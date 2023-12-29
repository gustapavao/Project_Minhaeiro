from django.shortcuts import redirect, render
from .models import *
from datetime import date

def app_minhaeiro(request):
    profile = Profile.objects.filter(user = request.user).first()
    expenses =  Expense.objects.filter(user = request.user)
    cards = CreditCard.objects.filter(user = request.user)
    if request.method == "POST":
        text = request.POST.get('text')
        amount = request.POST.get('amount')
        expense_type = request.POST.get('expense_type')
        card = request.POST.get('card')
        parcelas = request.POST.get('n_parcelas')


        expense = Expense(name=text , amount=amount , expense_type=expense_type , parcelas=parcelas , card=card , user=request.user)
        expense.save()

        if expense_type == "Adicionar":
            profile.balance += float(amount)
        if expense_type == "Retirar":
            profile.balance -= float(amount)
            profile.expenses += float(amount)

        profile.save()
        return redirect('/')
    
    context = {'profile':profile, 'expenses': expenses, 'cards':cards}
    return render(request, 'home.html', context)

def new_card(request):
    if request.method == "POST":
        name = request.POST.get('name')
        pay_day = request.POST.get('pay_day')
        close_fature = request.POST.get('close_fature')
        logo = request.POST.get('logo_card')

        card = CreditCard(name=name, pay_day=pay_day, logo=logo, close_fature=close_fature , user=request.user)
        card.save()
        return redirect('/  ')
    return render(request, 'add_new_card.html')