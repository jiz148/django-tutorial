from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse

from .models import Question


# Create your views here.
def index(request):
    latest_question_list = Question.objects.order_by('-pub_date')[:5]
    context = {
        'latest_question_list': latest_question_list,
    }
    return render(request=request, template_name='polls/index.html', context=context)


def detail(request, question_id):
    # if not exist, raise 404
    question = get_object_or_404(Question, pk=question_id)
    return render(request, 'polls/detail.html', {'question': question})


def results(request, question_id):
    response = "You're looking at the results of question %s"
    return HttpResponse(response % question_id)


def vote(request, question_id):
    return HttpResponse("You're voting on question %s" % question_id)


# coursera assignment
def owner(request):
    return HttpResponse("Hello, world. 8c0f24a3 is the polls index.")
