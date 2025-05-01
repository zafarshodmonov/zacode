from django.contrib import admin
from .models import Contest, Problem, Topic, TestCase


@admin.register(TestCase)
class TestCaseAdmin(admin.ModelAdmin):
    list_display = ['problem', 'input_data', 'expected_output']
    search_fields = ['problem__title']
    list_filter = ['problem__contest']

@admin.register(Contest)
class ContestAdmin(admin.ModelAdmin):
    list_display = ['title', 'start_time', 'end_time', 'is_public', 'is_active']
    search_fields = ['title']
    list_filter = ['is_public', 'is_active']


@admin.register(Topic)
class TopicAdmin(admin.ModelAdmin):
    list_display = ['title', 'created_at', 'updated_at']
    search_fields = ['title']


@admin.register(Problem)
class ProblemAdmin(admin.ModelAdmin):
    list_display = ['title', 'index', 'contest', 'difficulty_origin', 'time_limit_ms', 'memory_limit_mb']
    search_fields = ['title', 'index']
    list_filter = ['difficulty_source']
    filter_horizontal = ['topics']  # many-to-many uchun qulay multi-select
    readonly_fields = ['created_at', 'updated_at']
    fieldsets = (
        (None, {
            'fields': (
                'contest', 'title', 'index', 'statement',
                'input_spec', 'output_spec', 'constraints', 'note',
                'time_limit_ms', 'memory_limit_mb',
                'difficulty_origin', 'difficulty_source',
                'examples', 'topics', 'created_at', 'updated_at'
            )
        }),
    )
