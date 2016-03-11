from django.shortcuts import render
from django.contrib.auth import login, authenticate
from django.http import HttpResponseRedirect
from django.core.urlresolvers import reverse

from . forms import UserSignupForm

# Create your views here.

def index(request):
    return render(request, 'file_sharing_app/index.html', {})

def signup(request):
    # POST: create a new user
    if request.method == 'POST':
        # create a form instance and populate it with data from the request
        form = UserSignupForm(request.POST)
        if form.is_valid():
            new_user = form.save()
            new_user = authenticate(username=form.cleaned_data['username'],
                                    password=form.cleaned_data['password1'])
            login(request, new_user)
            return HttpResponseRedirect(reverse('file_sharing_app:index'))

    # GET: display the form to create a user
    else:
        form = UserSignupForm()

    return render(request, 'file_sharing_app/sign_up.html', {'form': form})
