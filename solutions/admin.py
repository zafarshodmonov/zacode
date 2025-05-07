from django.contrib import admin
from .models import Solution

@admin.register(Solution)
class SolutionAdmin(admin.ModelAdmin):
    list_display = ('id', 'problem', 'language', 'created_at')
    list_filter = ('language',)
    search_fields = ('problem__title', 'language')
