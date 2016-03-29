from django.shortcuts import get_object_or_404, render
from django.contrib.auth import login, authenticate
from django.contrib.auth.decorators import login_required
from django.http import HttpResponseRedirect
from django.core.urlresolvers import reverse

from . forms import UserSignupForm, AddGroupForm, GroupFileForm, GroupAddMemberForm
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
    if request.method == 'POST':
        add_group_form = AddGroupForm(request.POST)
        if add_group_form.is_valid():
            new_group = add_group_form.save(commit=False)
            new_group.creator = request.user
            new_group.save()
            return HttpResponseRedirect(reverse('file_sharing_app:group'))

    add_group_form = AddGroupForm()
    user_group = Group.objects.filter(creator=request.user)
    shared_group = Group.objects.filter(members=request.user)
    return render(request, 'file_sharing_app/group.html', {
        'user_group': user_group,
        'shared_group': shared_group,
        'add_group_form': AddGroupForm
    })

@login_required()
def group_detail(request, group_id):
    grp = get_object_or_404(Group, pk=group_id)
    if request.method == 'POST':
        if 'group_file_submit' in request.POST:
            group_file_form = GroupFileForm(request.POST, request.FILES)
            group_add_member_form = GroupAddMemberForm(initial={'group':grp.id})
            if group_file_form.is_valid():
                new_groupfile = group_file_form.save()
                return HttpResponseRedirect(reverse('file_sharing_app:group_detail', args=(new_groupfile.group.id,)))
        elif 'group_add_member_submit' in request.POST:
            group_file_form = GroupFileForm(initial={'group':grp.id})
            group_add_member_form = GroupAddMemberForm(request.POST)
            if group_add_member_form.is_valid():
                new_groupmember = group_add_member_form.save()
                return HttpResponseRedirect(reverse('file_sharing_app:group_detail', args=(new_groupmember.group.id,)))
    else:
        group_file_form = GroupFileForm(initial={'group':grp.id})
        group_add_member_form = GroupAddMemberForm(initial={'group':grp.id})
    return render(request, 'file_sharing_app/group_detail.html', {
        'group': grp,
        'group_file_form': group_file_form,
        'group_add_member_form': group_add_member_form
    })

