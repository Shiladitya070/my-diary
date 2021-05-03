from django.db import models
from taggit.managers import TaggableManager
# Create your models here.
class Note (models.Model):
    id = models.AutoField(primary_key=True)
    title = models.TextField(max_length=500,default='')
    content = models.TextField(max_length=10000,default='')
    tags = TaggableManager()
    created_at = models.DateTimeField(auto_now_add=True)
    def __str__(self):
        return self.title
    