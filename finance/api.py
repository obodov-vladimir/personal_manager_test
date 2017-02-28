from rest_framework import generics, permissions


from .serializers import IncomeSerializer
from .models import Income


class IncomeList(generics.ListCreateAPIView):
    queryset = Income.objects.all()
    serializer_class = IncomeSerializer
    permission_classes = [
        permissions.AllowAny
    ]

