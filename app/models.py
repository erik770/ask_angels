from django.db import models

# Create your models here.

class Question(models.Model):
    id = models.IntegerField
    avatar= models.FilePathField
    title = models.CharField(max_length = 256)
    text = models.TextField(400)
    best_ans = models.TextField(400)
    numb_of_ans = models.IntegerField
    like_counter = models.IntegerField
    dislike_counter = models.IntegerField
    creation_time = models.DateTimeField
    tags = models.ManyToManyField('Tag',related_name='questions')

class Tag(models.Model):
    tag_name = models.CharField(max_length=256)
