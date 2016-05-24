# -*- coding: utf-8 -*-

from django import forms
from django.contrib.auth.models import User

from qa.models import Question, Answer
from django.shortcuts import get_object_or_404


class AskForm(forms.Form):
    title = forms.CharField(label='Заголовок', max_length=200)
    text = forms.CharField(label='Текст вопроса', widget=forms.Textarea)

    def clean(self):
        pass

    def clean_message(self):
        pass

    def save(self, user):
        q = Question(**self.cleaned_data)
        #user, _ = User.objects.get_or_create(username='Max', password='111111')
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

    def save(self, user):
        answer = Answer() #**self.cleaned_data)
        answer.text = self.cleaned_data['text']
        question_id = self.cleaned_data['question']
        answer.question = get_object_or_404(Question, pk=question_id)
        # здесь нужно поправить. устанавливать пользователя из session.user
        #user, _ = User.objects.get_or_create(username='Max', password='111111')
        answer.author = user
        answer.save()
        return answer


class UserCreateForm(forms.Form):
    username = forms.CharField(required=True, widget=forms.TextInput)
    email = forms.EmailField(required=True, widget=forms.EmailInput)
    password = forms.CharField(required=True, widget=forms.PasswordInput)

    def clean(self):
        pass

    def clean_username(self):
        username = self.cleaned_data['username']
        try:
            u = User.objects.get(username=username)
        except User.DoesNotExist:
            return username
        raise forms.ValidationError('User has been registered!',
                code='BadUserName')

    def save(self):
        user = User.objects.create_user(self.cleaned_data["username"],
                self.cleaned_data["email"],
                self.cleaned_data["password"])
        user.save()
        return user


