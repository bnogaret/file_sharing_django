import logging

from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from django.utils.translation import ugettext as _

# Get an instance of a logger
logger = logging.getLogger(__name__)

from .models import GroupFile, GroupMembership

class UserSignupForm(UserCreationForm):
    """
    Add the email field to the form that is required.
    """
    email = forms.EmailField(required=True)

    class Meta:
        model = User
        fields = ("username", "email", "password1", "password2")

    def save(self, commit=True):
        user = super(UserSignupForm, self).save(commit=False)
        user.email = self.cleaned_data["email"]
        if commit:
            user.save()
        return user

class GroupFileForm(forms.ModelForm):
    class Meta:
        model = GroupFile
        fields = ('title', 'file', 'group')
        widgets = {
            'group': forms.HiddenInput(),
            'title': forms.TextInput(attrs={'class':'mdl-textfield__input'}),
            'file': forms.FileInput(attrs={'accept':".pdf,.odt,.tex,.docx,.doc"})
        }

class GroupAddMemberForm(forms.ModelForm):
    member = forms.CharField()
    member.widget = forms.TextInput(attrs={'class':'mdl-textfield__input'})

    class Meta:
        model = GroupMembership
        fields = ('member', 'group')
        widgets = {
            'group': forms.HiddenInput()
        }

    def clean_member(self):
        try:
            user = User.objects.get(username=self.cleaned_data['member'])
            return user
        except User.DoesNotExist:
            raise forms.ValidationError(_('Unknown user'))

    def clean(self):
        cleaned_data = super(GroupAddMemberForm, self).clean()
        user = cleaned_data['member']
        group = cleaned_data['group']

        logger.debug(user)
        logger.debug(group)

        if user and group:
            # If both fields are valid so far
            if group.creator == user or user in group.members.all():
                # raise forms.ValidationError(_('Try to add a user that is already in the group'))
                error = forms.ValidationError(_('Try to add a user that is already in the group'))
                self.add_error('member', error)
