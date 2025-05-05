from django.db import models
from datetime import timedelta
from django.contrib.auth.models import User

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


# --- Topic Model ---
class Topic(models.Model):
    title = models.CharField(max_length=255)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title

# --- Problem Model ---
class Problem(models.Model):
  
    contest = models.ForeignKey(Contest, related_name="problems", on_delete=models.CASCADE)
    title = models.CharField(max_length=255)
    index = models.CharField(max_length=10)  # A, B, C, D, etc.
    statement = models.TextField()
    input_spec = models.TextField()
    output_spec = models.TextField()
    note = models.TextField(null=True, blank=True)
    constraints = models.TextField(null=True, blank=True)
    time_limit_ms = models.IntegerField()
    memory_limit_mb = models.IntegerField()
    difficulty_origin = models.IntegerField()
    examples = models.JSONField()  # [{ "input": "", "output": "" }, ...]
    topics = models.ManyToManyField(Topic, related_name='problems', blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.title} ({self.index})"


# --- Test Case Model ---
class TestCase(models.Model):
    CATEGORY_CHOICES = [
        ('sample', 'Sample'),
        ('handmade', 'Handmade'),
        ('random', 'Random'),
        ('extreme', 'Extreme'),
        ('custom', 'Custom'),
    ]

    problem = models.ForeignKey(Problem, on_delete=models.CASCADE, related_name='testcases')
    input_data = models.TextField()
    expected_output = models.TextField()
    category = models.CharField(max_length=10, choices=CATEGORY_CHOICES, default='handmade')

    def __str__(self):
        return f"TestCase for {self.problem.title} ({self.category})"

# --- Contest Participant Model ---
class ContestParticipant(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    contest = models.ForeignKey(Contest, on_delete=models.CASCADE, related_name="participants")
    score = models.FloatField(default=0)
    rank = models.IntegerField(null=True, blank=True)
    rating_change = models.FloatField(default=0)

    joined_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        unique_together = ('user', 'contest')

    def __str__(self):
        return f"{self.user.username} in {self.contest.title}"
