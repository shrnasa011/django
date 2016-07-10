from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse, HttpResponseRedirect, Http404
from login.models import User
from django.core.urlresolvers import reverse
from django.utils import timezone
from django import forms
from django.forms import ModelForm, PasswordInput, modelform_factory
from django.views import generic
# Create your views here.

class NameForm(ModelForm):
    class Meta:
        model=User
        fields=['username', 'password']
        widgets={'password':PasswordInput}

def signup(request):
    if request.method=='POST':
        form=NameForm(request.POST)
        #check here
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse('poll:login'))
            #else:
                #Display error

    else:
        form=NameForm()

    #Return to the same page
    return render(request, 'login/signup.html', {'form':form,})

    
def login(request):
    if request.method=='POST':
        form=NameForm(request.POST)
        #check here
        if form.is_valid():
            user=User.objects.filter(username=form.cleaned_data['username'], password=form.cleaned_data['password'])
            if user:
                request.session['user']=form.cleaned_data['username']
                return HttpResponseRedirect(reverse('polls:index', ))
            else:
                return render(request, 'login/initial.html', {'form':form, 'error_message':"Invalid username or password",})

    else:
        form=NameForm()

    #Return to the same page
    return render(request, 'login/initial.html', {'form':form,})
        

def logout(request):
    try:
        del request.session['user']
    except KeyError:
        pass
    return render(request, 'login/logout.html')
