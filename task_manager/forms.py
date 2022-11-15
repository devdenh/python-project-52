from django import forms
from django.contrib.auth import get_user_model
from django.utils.translation import gettext as _
from django.contrib.auth.forms import AuthenticationForm


LOG_IN_ERROR_MESSAGE = _('Please, enter valid user name and password.'
                         ' Both fields might be register sensitive.')


class UserLoginForm(AuthenticationForm):
    username = forms.CharField(label=_('User name'),
                               required=True,
                               widget=forms.TextInput(
                                   attrs={'placeholder': _('User name'),
                                          'class': 'form-control'}))
    password = forms.CharField(label=_('Password'),
                               widget=forms.PasswordInput(
                                   attrs={'placeholder': _('Password'),
                                          'class': 'form-control'}))
    error_messages = {'invalid_login': LOG_IN_ERROR_MESSAGE}

    class Meta:
        model = get_user_model()
        fields = ['username', 'password']
