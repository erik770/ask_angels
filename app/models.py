from django.utils import timezone
from django.contrib.auth.models import AbstractUser
from django.contrib.contenttypes.models import ContentType
from django.contrib.contenttypes.fields import GenericForeignKey, GenericRelation
from django.db import models

import random, string


def random_word(length):
    letters = string.ascii_lowercase
    return ''.join(random.choice(letters) for i in range(length))

class ProfileManager(models.Manager):
    def best():
        return Profile.objects.all()  # todo sort best usr

class Profile(AbstractUser):
    avatar = models.ImageField(upload_to='uploads', default='avatar1.jpg') 


class TagManager(models.Manager):
    def best():
        return Tag.objects.all()  #todo sort popular

class Tag(models.Model):
    tag_name = models.CharField(max_length=50, unique=True)

    def __str__(self):
        return self.tag_name


class Vote(models.Model):
    votes = (
        (1, 'Like'),
        (-1, 'Dislike')
    )

    vote = models.SmallIntegerField(choices=votes)

    user = models.ForeignKey('Profile', on_delete=models.CASCADE, db_index=True)
    
    content_type = models.ForeignKey(ContentType, on_delete=models.CASCADE, default="")
    object_id = models.PositiveIntegerField(default=1)
    content_object = GenericForeignKey('content_type', 'object_id', 'vote')
    class Meta:
        unique_together = (("content_type", "object_id", "user"),)


class QuestionManager(models.Manager):
    def get_questions_by_tag(self, tag_name):
        tag = Tag.objects.get(tag_name=tag_name)
        return self.filter(tags=tag)

    def get_hot_questions(self):
        return self.order_by('-votes')  
    
    def get_new_questions(self):
        return self.order_by('-creation_time') 


class Question(models.Model):
    title = models.CharField(max_length = 256)
    question_text = models.TextField(1000)
    creation_time = models.DateTimeField(default=timezone.now)

    author = models.ForeignKey('Profile', on_delete=models.CASCADE)
    votes = GenericRelation('Vote', related_query_name='question')
    tags = models.ManyToManyField('Tag',related_name='question')
    objects = QuestionManager()
    
    def ans_count(self):
        return AnswerManager.get_by_question(self).count

    def likes_count(self):
        return self.votes.filter(vote='1').count()
    
    def dislikes_count(self):
        return self.votes.filter(vote='-1').count()




class AnswerManager(models.Manager):
    def get_by_question(self, question):
        return self.filter(question=question)


class Answer(models.Model):
    text = models.TextField(1000)
    is_correct = models.BooleanField(default=False)

    author = models.ForeignKey('Profile', on_delete=models.CASCADE, db_index=True)
    question = models.ForeignKey('Question', on_delete=models.CASCADE, db_index=True)
    votes = GenericRelation('Vote', related_query_name='answer')


    objects = AnswerManager()

    def likes_count(self):
        return self.votes.filter(vote='1').count()
    
    def dislikes_count(self):
        return self.votes.filter(vote='-1').count()