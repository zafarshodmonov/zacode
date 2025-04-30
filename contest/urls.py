from django.urls import path
from django.contrib import admin
from . import views

urlpatterns = [
    # Matches the root URL ("/") and calls the 'home' view
    path('', views.base, name='base'),
    path('admin/', admin.site.urls),
    path('problems/', views.problem_list, name='problem_list'),
    path('contests/', views.contest_list, name='contest_list'),
    path('topics/', views.topic_list, name='topic_list'),
    path('topics/<int:pk>/', views.topic_detail, name='topic_detail'),
    path('contests/<int:contest_id>/', views.contest_detail, name='contest_detail'),
    path('contests/<int:contest_id>/<str:problem_index>/', views.problem_detail, name='problem_detail'),
]
