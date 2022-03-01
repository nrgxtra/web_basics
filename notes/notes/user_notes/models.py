from django.db import models


class Note(models.Model):
    title = models.CharField(max_length=30)
    content = models.TextField()
    image_url = models.URLField()
    
