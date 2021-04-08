from django.db import models

class Program(models.Model):
    title = models.CharField(max_length=30)
    category = models.CharField(max_length=30)
    video_url = models.CharField(max_length=200)
    # number_of_views...
    # rating...
