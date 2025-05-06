from django.db import models
from datetime import timedelta

# --- Contest Model ---
class Contest(models.Model):

    class Meta:
        db_table = 'contest'

    DIVISION_CHOICES = [
        ('Div1', 'Division 1'),
        ('Div2', 'Division 2'),
        ('Div3', 'Division 3'),
        ('Div4', 'Division 4'),
        ('Open', 'Open for All'),
    ]

    VISIBILITY_CHOICES = [
        ('public', 'Public'),
        ('private', 'Private'),
    ]

    title = models.CharField(max_length=255)
    description = models.TextField()
    start_time = models.DateTimeField()
    duration_minutes = models.PositiveIntegerField(default=150)  # Duration in minutes
    end_time = models.DateTimeField(blank=True)

    def save(self, *args, **kwargs):
        if self.start_time and self.duration_minutes:
            self.end_time = self.start_time + timedelta(minutes=self.duration_minutes)
        super().save(*args, **kwargs)

    is_public = models.BooleanField(default=True)  # Public or Private contest
    is_active = models.BooleanField(default=True)  # Contest active status
    division = models.CharField(max_length=10, choices=DIVISION_CHOICES, default='Open')
    rated = models.BooleanField(default=True)  # Whether contest affects user ratings
    visibility = models.CharField(max_length=10, choices=VISIBILITY_CHOICES, default='public')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title
    
    @property
    def problems_count(self):
        return self.problems.count()

