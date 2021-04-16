from django.db import models
from django.db.models.deletion import CASCADE
from embed_video.fields import EmbedVideoField

class CategoryManager(models.Manager):
    def create_category(self, name):
        category = self.create(name=name)
        category.save(using=self._db)
        return category

class VideoManager(models.Manager):
    def create_exercise(self, title, category,added, url):
        video = self.create(
            title=title,
            category=category,
            added=added,
            url=url
        )
        video.save(using=self._db)
        return video

class Category(models.Model):
    name = models.CharField(max_length= 25)

    def __str__(self):
        return str(self.name)

class Video(models.Model):
    title = models.CharField(max_length=100)
    category = models.ForeignKey(Category, max_length=25, on_delete=models.CASCADE)
    added = models.DateTimeField(auto_now_add=True)
    url = EmbedVideoField()

    def __str__(self):
        return str(self.title)

    class Meta:
        ordering = ['-added']
