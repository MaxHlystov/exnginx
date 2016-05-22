# -*- coding: utf-8 -*-

from django.contrib.auth.models import User
from django import forms
from qa.models import Question


class AskForm(forms.Form):
    title = forms.CharField(label='Заголовок', max_length=200)
    text = forms.CharField(label='Текст вопроса', widget=forms.Textarea)

    def clean(self):
        pass

    def clean_message(self):
        pass

    def save(self):
        q = Question(**self.cleaned_data)
        user, _ = User.objects.get_or_create(username='Max', password='111111') 
        q.author = user
        q.save()
        return q


class AnswerForm(forms.Form):
    text = forms.CharField(label='Ответ', widget=forms.Textarea)
    question = forms.IntegerField()
    def clean(self):
        pass

    def clean_message(self):
        pass

    def save(self):
        pass


