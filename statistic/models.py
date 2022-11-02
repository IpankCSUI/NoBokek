from add.models import Money
from django.db import models
from django.contrib.auth.models import User

# Create your models here.
# class Stat(models.Model):
#     user = models.ForeignKey(to=User, on_delete=models.CASCADE)
#     income = models.FloatField()
#     outcome = models.FloatField()
#     date = models.DateField()
class Stat(models.Model):
    user = Money.user
    income = Money.income
    outcome = Money.outcome
    date = Money.date