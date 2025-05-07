from django.urls import path
from . import views

urlpatterns = [
    path('', views.solution_list, name='solution_list'),
]