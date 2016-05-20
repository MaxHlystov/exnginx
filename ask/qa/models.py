# -*- coding: utf-8 -*-


from __future__ import unicode_literals

from django.db import models
from django.contrib.auth.models import User

class QUser(models.Model):
    """Пользователь системы"""
    user = models.OneToOneField(User, on_delete=models.CASCADE)


class Question(models.Model):
    """Вопрос"""

    title = models.CharField(max_length=200) # заголовок вопроса
    text = models.TextField() # полный текст вопроса
    added_at = models.DateTimeField('date added') # дата добавления вопроса
    rating = models.IntegerField(default=0) # рейтинг вопроса (число)
    author = models.ForeignKey(QUser, on_delete=models.CASCADE) # автор вопроса
    # список пользователей, поставивших "лайк"
    likes = models.ManyToManyField(QUser,related_name="%(app_label)s_%(class)s_related")


class Answer(models.Model):
    """ответ"""

    text = models.TextField() # текст ответа
    added_at = models.DateTimeField() # дата добавления ответа
    # вопрос, к которому относится ответ
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    author = models.ForeignKey(QUser, on_delete=models.CASCADE) # автор ответа

