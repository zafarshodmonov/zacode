from django.contrib import admin
from .models import Problem

@admin.register(Problem)
class ProblemAdmin(admin.ModelAdmin):
    list_display = ('title', 'index', 'contest', 'difficulty_origin', 'time_limit_ms', 'memory_limit_mb')
    search_fields = ('title', 'index', 'contest__title')
    list_filter = ('difficulty_origin', 'contest')
    ordering = ('contest', 'index')
    filter_horizontal = ('topics',)  # many-to-many uchun multi-select ko'rinish
    readonly_fields = ('created_at', 'updated_at')
    fieldsets = (
        (None, {
            'fields': (
                'contest', 'title', 'index',
                'statement', 'input_spec', 'output_spec', 'constraints', 'note',
                'time_limit_ms', 'memory_limit_mb',
                'difficulty_origin',
                'examples', 'topics',
                'created_at', 'updated_at',
            ),
        }),
    )