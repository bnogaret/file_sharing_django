from django.shortcuts import render
from django.contrib.auth import login, authenticate
from django.contrib.auth.decorators import login_required
from django.http import HttpResponseRedirect
from django.core.urlresolvers import reverse

from . forms import UserSignupForm
from . models import Group

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

@login_required()
def group(request):
    user_group = Group.objects.filter(creator=request.user)
    shared_group = Group.objects.filter(members=request.user)
    return render(request, 'file_sharing_app/group.html', {
        'user_group': user_group,
        'shared_group': shared_group
    })
