from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from .models import Question
from django.http import Http404


def index(request):
    latest_questions = Question.objects.order_by('-pub_date')[:5]
    template = 'polls/index.html'
    context = {
        'latest_questions': latest_questions
    }
    return render(request, template, context)


def detail(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    template = 'polls/detail.html'
    return render(request, template, {'question': question})


def results(request, question_id):
    return HttpResponse(f"You are looking at the results of question {question_id}")


def vote(request, question_id):
    return HttpResponse(f"You are looking fot voting on question {question_id}")
