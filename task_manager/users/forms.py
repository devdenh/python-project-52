from django.contrib.auth.forms import UserCreationForm
from django.utils.translation import gettext as _
from django.contrib.auth import get_user_model
from django import forms


class UserForm(forms.ModelForm):

    class Meta:
        model = get_user_model()
        fields = ['first_name', 'last_name', 'username']


class RegisterUserForm(UserCreationForm):
    first_name = forms.CharField(label=_('First name'),
                                 required=True,)

    last_name = forms.CharField(label=_('Last name'),
                                required=True,)

    username = forms.CharField(label=_('User Name'),
                               required=True)

    password1 = forms.CharField(label=_('Password'),
                                required=True,
                                widget=forms.PasswordInput(attrs={'class': 'form-input'})),

    password2 = forms.CharField(label=_('Repeat Password'),
                                required=True,
                                widget=forms.PasswordInput(attrs={'class': 'form-input'}))

    class Meta:
        model = get_user_model()
        fields = ['first_name', 'last_name', 'username', 'password1', 'password2']
