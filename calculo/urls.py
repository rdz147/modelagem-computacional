# calculo/urls.py
from django.urls import path
from .views import home_calculo_view, newton_calculator_view, bissecao_calculator_view

urlpatterns = [
    path('', home_calculo_view, name='home_calculo'),
    path('newton/', newton_calculator_view, name='newton_calculator'),
    path('bissecao/', bissecao_calculator_view, name='bissecao_calculator'),
]