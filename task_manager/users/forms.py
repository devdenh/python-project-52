from django.contrib.auth.forms import UserCreationForm
from django.utils.translation import gettext as _
from django.contrib.auth import get_user_model
from django.utils.safestring import mark_safe
from django.utils.html import format_html
from django import forms


USERNAME_FIELD_SESCRIPTION = _("Обязательное поле. "
                               "Не более 150 символов. "
                               "Только буквы, цифры и символы @/./+/-/_.")
PASSWORD_REQUIREMENTS_MESSAGE = _("Ваш пароль должен содержать как минимум 3 символа.")
REPEAT_PASSWORD_MESSAGE = _("Для подтверждения введите, пожалуйста, пароль ещё раз.")


class RegisterUserForm(UserCreationForm):

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        as_ul = format_html("<ul>{}</ul>",
                            format_html("<li>{}</li>",
                                        PASSWORD_REQUIREMENTS_MESSAGE))
        self.fields["password1"].help_text = as_ul
        self.fields["password2"].help_text = REPEAT_PASSWORD_MESSAGE

    first_name = forms.CharField(label=_('First name'),
                                 required=True,)

    last_name = forms.CharField(label=_('Last name'),
                                required=True,)

    username = forms.CharField(label=_('User Name'),
                               required=True,
                               help_text=USERNAME_FIELD_SESCRIPTION)

    password1 = forms.CharField(label=_('Password'),
                                required=True,
                                help_text=PASSWORD_REQUIREMENTS_MESSAGE,
                                widget=forms.PasswordInput(
                                    attrs={'class': 'form-input',
                                           "help_text": PASSWORD_REQUIREMENTS_MESSAGE}),
                                ),

    password2 = forms.CharField(label=_('Repeat Password'),
                                required=True,
                                widget=forms.PasswordInput(attrs={'class': 'form-input'}))

    class Meta:
        model = get_user_model()
        fields = ['first_name', 'last_name', 'username', 'password1', 'password2']
