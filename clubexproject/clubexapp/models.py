from django.db import models

class Exercise(models.Model):
    name = models.CharField(max_length=30)
    category = models.CharField(max_length=30)
    video_url = models.CharField(max_length=30)
    # number_of_views...
    # rating...
