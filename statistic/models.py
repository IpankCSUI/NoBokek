from audioop import add
from django.db import models
from add.models import Money

# Create your models here.
class Stat(models.Model):
    user = Money.user
    income = Money.income
    outcome = Money.outcome
    date = Money.date