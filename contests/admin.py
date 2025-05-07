from django.contrib import admin
from .models import Contest

@admin.register(Contest)
class ContestAdmin(admin.ModelAdmin):
    list_display = ('title', 'start_time', 'end_time', 'is_public', 'is_active')
    search_fields = ('title',)
    list_filter = ('is_public', 'is_active')
    ordering = ('-start_time',)
    date_hierarchy = 'start_time'
    readonly_fields = ('created_at', 'updated_at')