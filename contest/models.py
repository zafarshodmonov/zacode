from django.db import models
from django.contrib.auth.models import User

# --- Contest Model ---
class Contest(models.Model):
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
    end_time = models.DateTimeField()
    is_public = models.BooleanField(default=True)  # Public or Private contest
    is_active = models.BooleanField(default=True)  # Contest active status
    division = models.CharField(max_length=10, choices=DIVISION_CHOICES, default='Open')
    rated = models.BooleanField(default=True)  # Whether contest affects user ratings
    visibility = models.CharField(max_length=10, choices=VISIBILITY_CHOICES, default='public')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title

# --- Topic Model ---
class Topic(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title

# --- Problem Model ---
class Problem(models.Model):
    DIFFICULTY_SOURCE_CHOICES = [
        ('codeforces', 'Codeforces'),
        ('zacode', 'ZaCode'),
        ('other', 'Other'),
    ]

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
    difficulty_source = models.CharField(max_length=50, choices=DIFFICULTY_SOURCE_CHOICES, default='zacode')
    examples = models.JSONField()  # [{ "input": "", "output": "" }, ...]
    topics = models.ManyToManyField(Topic, related_name='problems', blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.title} ({self.index})"

    def get_normalized_difficulty(self):
        """
        Returns normalized difficulty between 0 and 100 based on source.
        """
        if self.difficulty_source == "codeforces":
            min_diff = 400
            max_diff = 3500
            return min(max((self.difficulty_origin - min_diff) * 100 / (max_diff - min_diff), 0), 100)
        else:
            return self.difficulty_origin

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
