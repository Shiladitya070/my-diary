from django.db import models
from taggit.managers import TaggableManager
from django.contrib.auth.models import User
from django.contrib.auth import get_user_model
from django.template.defaultfilters import slugify
from django.urls import reverse
import string
import random
User = get_user_model()

def rand_slug():
    return ''.join(random.choice(string.ascii_letters + string.digits) for _ in range(6))
# Create your models here.
class Note (models.Model):
    
    title = models.TextField(max_length=500,default='')
    content = models.TextField(default='')
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    slug = models.SlugField(max_length=1000, blank=True)
    tags = TaggableManager()
    created_at = models.DateTimeField(auto_now_add=True)
    def __str__(self):
        return self.title
    def save(self, *args, **kwargs):
        if not self.slug:
            # self.slug = slugify(self.title)
            self.slug = slugify(rand_slug() + "-" + self.title)
        return super(Note, self).save(*args, **kwargs)
    def get_absolute_url(self):
        return reverse('note-show', kwargs={'slug': self.slug})
    