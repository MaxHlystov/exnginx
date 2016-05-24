# -*- coding: utf-8 -*-

from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse, HttpResponseRedirect
from django.core.paginator import Paginator
from django.http import Http404
from django.views.decorators.http import require_GET, require_POST
from django.contrib.auth.decorators import login_required
from django.contrib.auth import login, authenticate
from django.utils.decorators import method_decorator
from django.core.urlresolvers import reverse
from django.views.generic.edit import FormView
from django.contrib.auth.forms import UserCreationForm

from qa.models import Question, Answer, User
from qa.forms import AskForm, AnswerForm, UserCreateForm


def paginate(request, qs):
    try:
        limit = int(request.GET.get('limit', 10))
    except ValueError:
        limit = 10
    if limit > 10:
        limit = 10
    page = request.GET.get('page') or 1
    try:
        page = int(request.GET.get('page', 1))
    except ValueError:
        raise Http404
    paginator = Paginator(qs, limit)
    try:
        page = paginator.page(page)
    except:
        page = paginator.page(paginator.num_pages)
    return page


@require_GET
def test(request, *args, **kwargs):
    return HttpResponse('OK')


@require_GET
def new_questions(request):
    """ Страница с новыми вопросами.
    Главная страница. Список "новых" вопросов. Т.е. последний заданный вопрос - первый в списке.
    На этой странице должна работать пагинация. Номер страницы указывается в GET параметре page.
    На страницу выводится по 10 вопросов. В списке вопросов должны выводится заголовки (title)
    вопросов и ссылки на страницы отдельных вопросов.
    """
    qs = Question.objects.order_by('-id')
    page = paginate(request, qs)
    return render(request, 'qa/questions.html', {'page': page})


@require_GET
def popular_questions(request):
    """ Страница с популярными вопросами.
    Cписок "популярных" вопросов. Сортировка по убыванию поля rating. На этой странице должна
    работать пагинация. Номер страницы указывается в GET параметре page.  На страницу выводится
    по 10 вопросов. В списке вопросов должны выводится заголовки (title) вопросов и ссылки на
    страницы отдельных вопросов.
    """
    qs = Question.objects.order_by('-rating')
    page = paginate(request, qs)
    return render(request, 'qa/questions.html', {'page': page})


def question(request, question_id):
    """ Страница одного вопроса.
    На этой странице должны выводится заголовок (title), текст (text) вопроса и все ответы на данный
    вопрос, без пагинации. В случае неправильного id вопроса view должна возвращать 404.
    """
    #if request.method == 'GET':
    question = get_object_or_404(Question, pk=question_id)
    form = AnswerForm() #initial={'question': question.id})
    form.fields['question'].initial = question.id
    return render(request, 'qa/question.html',
            {'question': question,
             'form': form})


@login_required()
def ask(request):
    """ Страница добавления вопроса.
    При GET запросе - отображается форма AskForm,
    при POST запросе форма должна создавать новый вопрос
    и перенаправлять на страницу вопроса - /question/123/
    """
    if request.method == 'POST':
        form = AskForm(request.POST)
        form._user = request.user
        if form.is_valid():
            q = form.save(request.user)
            url = reverse('question', args=(q.id,))
            return HttpResponseRedirect(url)
    else:
        form = AskForm()
    return render(request, 'qa/ask.html', {'form': form})


@login_required()
@require_POST
def answer(request):
    """ Страница добавления ответа.
    При POST запросе форма AnswerForm добавляет новый ответ
    и перенаправляет на страницу вопроса /question/123/
    """
    form = AnswerForm(request.POST)
    if form.is_valid():
        answer = form.save(request.user)
        url = reverse('question', args=(answer.question.id,))
        return HttpResponseRedirect(url)
    return render(request, 'qa/answer.html', {'form': form})


def signup(request):
    if request.method == 'POST':
        form = UserCreateForm(request.POST)
        if form.is_valid():
            user = form.save()
            user = authenticate(username=form.cleaned_data['username'],
                    password=form.cleaned_data['password'])
            if user is not None:
                login(request, user)
                url = reverse('main')
            else:
                url = reverse('login')
            return HttpResponseRedirect(url)
    else:
        form = UserCreateForm()
    return render(request, 'qa/signup.html', {'form': form})




