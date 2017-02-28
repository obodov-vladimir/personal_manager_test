from django.db import models


class Income(models.Model):
    name = models.CharField(max_length=200)
    income_date = models.DateTimeField('date of income')
    amount = models.IntegerField(default=0)
