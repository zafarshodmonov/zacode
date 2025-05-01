# contest/models.py
from django.db import models

class Contest(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField()  # description of the contest
    start_time = models.DateTimeField()  # start time of the contest
    end_time = models.DateTimeField()  # end time of the contest
    is_public = models.BooleanField(default=True)  # public or private contest
    is_active = models.BooleanField(default=True)  # active or inactive contest
    created_at = models.DateTimeField(auto_now_add=True)  # creation timestamp
    updated_at = models.DateTimeField(auto_now=True)  # last updated timestamp
    # slug = models.SlugField(unique=True, blank=True, null=True)  # optional for URL structure

    def __str__(self):
        return self.title
    
class Topic(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title


class Problem(models.Model):
    contest = models.ForeignKey(Contest, related_name="problems", on_delete=models.CASCADE)
    title = models.CharField(max_length=255)
    index = models.CharField(max_length=10)
    statement = models.TextField()
    input_spec = models.TextField()
    output_spec = models.TextField()
    note = models.TextField(null=True, blank=True)
    constraints = models.TextField(null=True, blank=True)
    time_limit_ms = models.IntegerField()
    memory_limit_mb = models.IntegerField()
    difficulty_origin = models.IntegerField()
    difficulty_source = models.CharField(max_length=50)
    examples = models.JSONField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    topics = models.ManyToManyField(Topic, related_name='problems', blank=True)

    def __str__(self):
        return f"{self.title} ({self.index})"

    def get_normalized_difficulty(self):

        if self.difficulty_source == "codeforces":
            min_diff = 400
            max_diff = 3500
            return min(max((self.difficulty_origin - min_diff) * 100 / (max_diff - min_diff), 0), 100)
        else:
            return self.difficulty_origin
        

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

