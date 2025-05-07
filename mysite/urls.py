from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include(('base.urls', 'base'), namespace='base')),
    path('problems/', include(('problems.urls', 'problems'), namespace='problems')),
    path('solutions/', include(('solutions.urls', 'solutions'), namespace='solutions')),
    path('topics/', include(('topics.urls', 'topics'), namespace='topics')),
    path('contests/', include(('contests.urls', 'contests'), namespace='contests')),
]
