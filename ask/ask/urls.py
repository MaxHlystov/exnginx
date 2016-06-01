# -*- coding: utf-8 -*-

"""ask URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.9/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url
from django.contrib import admin
from django.contrib.auth.views import login, logout
from qa import views

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^$', views.new_questions, name='main'),
    url(r'^signup/', views.signup, name='signup'),
    url(r'^logout/', logout),
    url(r'^login/', login,
        {'template_name': 'qa/login.html'},
        name='login'),
    url(r'^question/(?P<question_id>[0-9]+)/$', views.question, name='question'),
    url(r'^ask/', views.ask, name='ask'),
    url(r'^answer/', views.answer, name='answer'),
    url(r'^popular/', views.popular_questions, name='popular_questions'),
    url(r'^new/', views.new_questions, name='new_questions'),
    url(r'^comments/(?P<answer_id>)/$', views.ajax_answers, name='ajax_answers'),
]

