from django.db import models
from django.utils import timezone

CHARS_MAX_LENGTH: int = 150

# Create your models here.

class Tag(models.Model):
    name = models.CharField(max_length=CHARS_MAX_LENGTH, blank=True)
    description = models.TextField(blank=True, null=True)

    def __str__(self):
        return self.name 



class Category(models.Model):
    name = models.CharField(max_length=CHARS_MAX_LENGTH, blank=True)
    description = models.TextField(blank=True, null=True)

    def __str__(self):
        return self.name


class Movie(models.Model):
    name = models.CharField(max_length=CHARS_MAX_LENGTH, blank=True)
    description = models.TextField(blank=True, null=True)
    date_created = models.DateTimeField(default=timezone.now)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    tags = models.ManyToManyField(Tag)
    watch_count = models.IntegerField(default=0)
    file = models.FileField(upload_to='movies/')
    preview_image = models.ImageField(upload_to='preview_images/')


    def __str__(self):
        return self.name 

