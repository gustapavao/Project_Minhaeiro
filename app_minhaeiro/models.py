from django.db import models
from django.contrib.auth.models import User
from datetime import date
# Create your models here.

TYPE = (

    ('Adicionar', 'Positivo'),
    ('Retirar', 'Negativo')
)

class Profile(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    income = models.FloatField()
    balance = models.FloatField(blank= True, null = True)
    expenses = models.FloatField(default = 0 )
    
class CreditCard(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    pay_day = models.DateField()
    logo = models.ImageField()
    def next_payday():
        pass
    def divisor_per_month(self, valor, parcelas):
        value_per_month = float(valor)/parcelas
        return value_per_month
    

        
    
class Expense(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    amount = models.FloatField()
    expense_type = models.CharField(max_length=100, choices=TYPE)
    date = models.DateField(default = date.today())
    parcelado = models.BooleanField()

    def __str__(self):
        return self.name

