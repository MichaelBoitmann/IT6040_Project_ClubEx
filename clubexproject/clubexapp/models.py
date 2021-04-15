from django.db import models

from embed_video.fields import EmbedVideoField

#***un-used model for now ***#

class Program(models.Model):
   title = models.CharField(max_length=30)
   category = models.CharField(max_length=30)
   video_url = models.CharField(max_length=200)
    # number_of_views...
    # rating...

class Video(models.Model):
    title = models.CharField(max_length=100)
    #category = models.CharField(max_length=30)
    added = models.DateTimeField(auto_now_add=True)
    url = EmbedVideoField()

    def __str__(self):
        return str(self.title)

    class Meta:
        ordering = ['-added']
