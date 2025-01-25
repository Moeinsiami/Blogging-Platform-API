from django.db import models
from django.contrib.postgres.fields import ArrayField


# class Tag(models.Model):
#     name = models.CharField(max_length=50, unique=True)
#
#     def __str__(self):
#         return self.name


class Post(models.Model):
    title = models.CharField(max_length=200)
    content = models.TextField()
    category = models.CharField(max_length=100)
    tags = models.JSONField(default=list)  # Default to an empty list
    createdAt = models.DateTimeField(auto_now=True)
    updatedAt = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title
