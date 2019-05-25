from django.urls import path
from . import views

app_name = 'main'
urlpatterns = [
    path('', views.index, name='index'),
    path('ask_question/', views.get_question, name='get_question'),
    path('order_printing/', views.get_printing_order, name='get_printing_order'),
    path('order_modeling/', views.get_modeling_order, name='get_modeling_order'),
]