# -*- coding: utf-8 -*-

from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from django.core.paginator import Paginator
from qa.models import Question, Answer
from django.http import Http404
from django.views.decorators.http import require_GET


def test(request, *args, **kwargs):
    return HttpResponse('OK')


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


@require_GET
def question(request, question_id):
    """ Страница одного вопроса.
    На этой странице должны выводится заголовок (title), текст (text) вопроса и все ответы на данный
    вопрос, без пагинации. В случае неправильного id вопроса view должна возвращать 404.
    """
    question = get_object_or_404(Question, pk=question_id)
    return render(request, 'qa/question.html', {'question': question})
            
