from django.shortcuts import render_to_response
from rest_framework import viewsets


def index(request):
    return render_to_response('finance/index.html')


def budget(request):
    return render_to_response('finance/budget.html')

from finance.serializers import IncomeSerializer
from finance.models import Income


class IncomeViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = Income.objects.all().order_by('-date_joined')
    serializer_class = IncomeSerializer

