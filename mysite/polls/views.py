from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse, HttpResponseRedirect, Http404
from polls.models import Question, Choice
from django.core.urlresolvers import reverse
from django.utils import timezone
from django import forms
from django.views import generic

# Create your views here.


#def index(request):
#    latest_ques=Question.objects.order_by('-pub_date')[:5]
#    output=', '.join([p.question_text for p in latest_ques])
#    return render(request, 'polls/index.html', {'latest_question_list':latest_ques})

#def detail(request, question_id):
#    question=get_object_or_404(Question, pk=question_id)
#    return render(request, 'polls/detail.html', {'question':question})

#def results(request, question_id):
#    question = get_object_or_404(Question, pk=question_id)
#    return render(request, 'polls/results.html', {'question': question})

class IndexView(generic.ListView):
    template_name='polls/index.html'
    context_object_name='latest_question_list'

    def get_queryset(self):
        return Question.objects.filter(pub_date__lte=timezone.now()).order_by("-pub_date")[:5]

def index(request):
    if request.session['user']:
        latest_ques=Question.objects.order_by('-pub_date')[:5]
        output=', '.join([p.question_text for p in latest_ques])
        return render(request, 'polls/index.html', {'latest_question_list':latest_ques})

    else:
        return HttpResponse("You are not logged in")

def detail(request, question_id):
    if request.session['user']:
        question=get_object_or_404(Question, pk=question_id)
        return render(request, 'polls/detail.html', {'question':question})

    else:
        return HttpResponse("You are not logged in")

def results(request, question_id):
    if request.session['user']:
        question = get_object_or_404(Question, pk=question_id)
        return render(request, 'polls/results.html', {'question': question})

    else:
        return HttpResponse("You are not logged in")


class DetailView(generic.DetailView):
    model=Question
    template_name='polls/detail.html'
    def get_queryset(self):
        return Question.objects.filter(pub_date__lte=timezone.now())

class ResultsView(generic.DetailView):
    model=Question
    template_name='polls/results.html'
    
def vote(request, question_id):
    p=get_object_or_404(Question, pk=question_id)
    try:
        selected_choice=p.choice_set.get(pk=request.POST['choice'])
    except(KeyError, Choice.DoesNotExist):
        return render(request, 'polls/detail.html', {'question':p, 'error_message':"You didn't select a choice.",})
    else:
        selected_choice.votes+=1;
        selected_choice.save()
                                    
        return HttpResponseRedirect(reverse('polls:results', args=(p.id,)))

