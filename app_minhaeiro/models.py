from django.db import models
from django.contrib.auth.models import User
from datetime import date, timezone, timedelta
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
    logo = models.ImageField(upload_to='uploads/')
    close_fature = models.DateField()
    def next_payday():
        agora = date.now()
        pass
    

        
    
class Expense(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    amount = models.FloatField()
    expense_type = models.CharField(max_length=100, choices=TYPE, blank=True, null=True)
    date = models.DateField(auto_now_add=True, blank=True, null=True)
    parcelas = models.FloatField(blank=True, null=True)
    card = CreditCard()
    
    def divisor_per_month(self):
        value_per_month = self.amount/self.parcelas
        return value_per_month
    
    valor_parcela = divisor_per_month()
    
    def __str__(self):
        return self.name