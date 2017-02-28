from django.conf.urls import url
from . import views
from .api import IncomeList

app_name = 'finance'

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^budget/', views.budget, name='budget'),
    url(r'^income/', IncomeList.as_view()),
]
