from .models import Income
from rest_framework import serializers


class IncomeSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Income
        fields = ('amount', 'income_date', 'name')

