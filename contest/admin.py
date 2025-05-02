# contest/admin.py

from django.contrib import admin
from .models import Contest, Problem, Topic, TestCase

@admin.register(Contest)
class ContestAdmin(admin.ModelAdmin):
    list_display = ('title', 'start_time', 'end_time', 'is_public', 'is_active')
    search_fields = ('title',)
    list_filter = ('is_public', 'is_active')
    ordering = ('-start_time',)
    date_hierarchy = 'start_time'
    readonly_fields = ('created_at', 'updated_at')

@admin.register(Topic)
class TopicAdmin(admin.ModelAdmin):
    list_display = ('title', 'created_at', 'updated_at')
    search_fields = ('title',)
    ordering = ('title',)
    readonly_fields = ('created_at', 'updated_at')

@admin.register(Problem)
class ProblemAdmin(admin.ModelAdmin):
    list_display = ('title', 'index', 'contest', 'difficulty_origin', 'difficulty_source', 'time_limit_ms', 'memory_limit_mb')
    search_fields = ('title', 'index', 'contest__title')
    list_filter = ('difficulty_source', 'contest')
    ordering = ('contest', 'index')
    filter_horizontal = ('topics',)  # many-to-many uchun multi-select ko'rinish
    readonly_fields = ('created_at', 'updated_at')
    fieldsets = (
        (None, {
            'fields': (
                'contest', 'title', 'index',
                'statement', 'input_spec', 'output_spec', 'constraints', 'note',
                'time_limit_ms', 'memory_limit_mb',
                'difficulty_origin', 'difficulty_source',
                'examples', 'topics',
                'created_at', 'updated_at',
            ),
        }),
    )

@admin.register(TestCase)
class TestCaseAdmin(admin.ModelAdmin):
    list_display = ('problem', 'category', 'short_input', 'short_output')
    search_fields = ('problem__title',)
    list_filter = ('problem__contest', 'category')
    ordering = ('problem',)

    # input va outputni qisqartirib ko'rsatish (uzun matnlar admin sahifani buzmasin deb)
    def short_input(self, obj):
        return (obj.input_data[:50] + '...') if len(obj.input_data) > 50 else obj.input_data
    short_input.short_description = "Input (short)"

    def short_output(self, obj):
        return (obj.expected_output[:50] + '...') if len(obj.expected_output) > 50 else obj.expected_output
    short_output.short_description = "Output (short)"
