from django.db import models
from contests.models import Contest
from topics.models import Topic


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
