from django.urls import path
from django.contrib import admin
from . import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('contests/', views.contest_list, name='contest_list'),
    path('contests/<int:contest_id>/', views.contest_detail, name='contest_detail'),
    path('contests/<int:contest_id>/<str:problem_index>/', views.problem_detail, name='problem_detail'),
]
