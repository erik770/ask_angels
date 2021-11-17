
import random
from random import randint

from faker import Faker

from app.models import *

f = Faker()


def fill_profiles(cnt):
    for i in range(cnt):
        Profile.objects.create(user=f.name())


def fill_tags(cnt):
    for i in range(cnt):
        Tag.objects.create(tag_title=f.word().lower())


def fill_questions(cnt):
    author_ids = list(Profile.objects.all())
    tag_names_list = [tag.tag_title for tag in Tag.objects.all()]
    tags_limit = 5
    for i in range(cnt):
        author_id = f.random.choice(author_ids)
        tags = f.random.sample(tag_names_list, randint(0, tags_limit))
        title = f.sentence(20)[:19]
        text = f.text(150)[:149]

        question = Question.objects.create_question(
            author=author_id,
            title=title,
            text=text,
            tag_names=tags)

        question.question_author.save()
        question.save()


def fill_likes(cnt, amount_of_questions, amount_of_comments):
    author_ids = list(Profile.objects.all())
    amount_of_authors = len(author_ids)
    likes_per_author = int(cnt / amount_of_authors)
    for i in range(amount_of_authors):
        for j in range(likes_per_author):
            if i % 2 == 1:
                vote = 1
                user = author_ids[i]
                content_type = ContentType.objects.get(app_label='app', model='question')
                object_id = random.uniform(j, amount_of_questions)
                Vote.objects.create(vote=vote, user=user, content_type=content_type, object_id=object_id)
            if i % 2 == 0:
                vote = -1
                user = author_ids[i]
                content_type = ContentType.objects.get(app_label='app', model='comment')
                object_id = random.uniform(j, amount_of_comments)
                Vote.objects.create(vote=vote, user=user, content_type=content_type, object_id=object_id)


def fill_answers(cnt):
    author_ids = list(Profile.objects.all())
    question_ids = list(Question.objects.all())
    for i in range(cnt):
        author_id = f.random.choice(author_ids)
        question_id = f.random.choice(question_ids)
        text = f.text(150)[:149]
        Answer.objects.create(comment_author=author_id,
                                question=question_id,
                                comment_text=text)


fill_tags(100000)
print("tags filled")
fill_profiles(10000)
print("profiles filled")
fill_questions(100000)
print("questions filled")
fill_answers(1000000)
print("comments filled")
fill_likes(2000000, 100000, 1000000)
print("likes filled")