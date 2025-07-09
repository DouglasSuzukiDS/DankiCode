from django.urls import path
# from notas.views import index
from . import views

urlpatterns = [
   path('', views.index, name='index')
]