# -*- coding: utf-8 -*-


from __future__ import unicode_literals
import datetime as datetime

from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone


class QuestionManager(models.Manager):
    def new():
        pass

    def popular():
        pass


class Question(models.Model):
    """Вопрос"""

    #objects = QuestionManager()
    title = models.CharField(max_length=200) # заголовок вопроса
    text = models.TextField() # полный текст вопроса
    added_at = models.DateTimeField('date added',auto_now_add=True) # дата добавления вопроса
    rating = models.IntegerField(default=0) # рейтинг вопроса (число)
    author = models.ForeignKey(User, on_delete=models.CASCADE) # автор вопроса
    # список пользователей, поставивших "лайк"
    likes = models.ManyToManyField(User,related_name="%(app_label)s_%(class)s_related")

    def __str__(self):
        return self.title

    def was_published_recently(self):
        return self.added_at >= timezone.now() - datetime.timedelta(days=1)


class Answer(models.Model):
    """ответ"""

    text = models.TextField() # текст ответа
    added_at = models.DateTimeField(auto_now_add=True) # дата добавления ответа
    # вопрос, к которому относится ответ
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    author = models.ForeignKey(User, on_delete=models.CASCADE) # автор ответа

    def __str__(self):
        return self.text

