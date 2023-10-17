from django.db import models

# Create your models here.
class Post(models.Model):
    id      = models.AutoField(primary_key=True)
    title   = models.CharField(max_length=100)
    author  = models.CharField(max_length=20)
    coverimg = models.FileField(max_length=100)
    created_at = models.DateTimeField(auto_now=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.id


class Contents(models.Model):
    id = models.AutoField(primary_key=True)
    wt = models.ForeignKey(Post, on_delete=models.CASCADE)
    contents = models.TextField()

    def __str__(self):
        return self.id