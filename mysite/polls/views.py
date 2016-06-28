from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse, Http404
from polls.models import Question, Choice

# Create your views here.
def index(request):
    latest_ques=Question.objects.order_by('-pub_date')[:5]
#    output=', '.join([p.question_text for p in latest_ques])
    return render(request, 'polls/index.html', {'latest_question_list':latest_ques})

def detail(request, question_id):
    question=get_object_or_404(Question, pk=question_id)
    return render(request, 'polls/detail.html', {'question':question})

def results(request, question_id):
    return HttpResponse("You're looking at the results of question %s."%question_id)

def vote(request, question_id):
    return HttpResponse("You're voting on question %s."%question_id)

