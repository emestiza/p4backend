from django.db import models
from authentication.models import User

# when editing models, MAKE MIGRATIONS AFTER

# Create your models here.
class Subject(models.Model):
    class Meta:
        verbose_name_plural = 'subjects'

    name = models.CharField(max_length = 100)
    owner = models.ForeignKey(User, on_delete = models.CASCADE)
    description = models.TextField(blank = True)
    created_at = models.DateTimeField(auto_now_add = True)
    updated_at = models.DateTimeField(auto_now = True)

    def __str__(self):
        return self.name

class Topic(models.Model):
    name = models.CharField(max_length = 100)
    owner = models.ForeignKey(User, on_delete = models.CASCADE)
    subject = models.ForeignKey(Subject, related_name = 'topics', on_delete = models.CASCADE)
    description = models.TextField(blank = True)
    created_at = models.DateTimeField(auto_now_add = True)
    updated_at = models.DateTimeField(auto_now = True)
    is_public = models.BooleanField(default = False)

    def __str__(self):
        return self.name

