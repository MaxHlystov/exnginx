# -*- coding: utf-8 -*-

from django.contrib.auth.models import User
from django import forms
from qa.models import Question, Answer
from django.shortcuts import get_object_or_404


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
    question = forms.IntegerField(widget=forms.HiddenInput )

    def clean(self):
        pass

    def clean_message(self):
        pass

    def save(self):
        answer = Answer() #**self.cleaned_data)
        answer.text = self.cleaned_data['text']
        question_id = self.cleaned_data['question']
        answer.question = get_object_or_404(Question, pk=question_id)
        # здесь нужно поправить. устанавливать пользователя из session.user
        user, _ = User.objects.get_or_create(username='Max', password='111111') 
        answer.author = user
        answer.save()
        return answer

