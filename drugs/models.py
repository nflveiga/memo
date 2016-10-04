from django.db import models
from ckeditor.fields import RichTextField

# Create your models here.

class Drug(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    name = models.CharField(max_length=100)
    category = models.CharField(max_length=100, null=True)
    content = RichTextField()
    def __unicode__(self):
        return self.name