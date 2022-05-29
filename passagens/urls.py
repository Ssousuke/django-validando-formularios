from django.urls import path
from . import views

app_name = 'passagens'
urlpatterns = [
    path('', views.index, name='home'),
    path('detalhes/', views.detalhes, name='detalhes'),
]
