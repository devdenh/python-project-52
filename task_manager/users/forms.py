from django.contrib.auth.forms import UserCreationForm
from django.utils.translation import gettext as _
from django.contrib.auth import get_user_model
from django.utils.html import format_html
from django import forms

from task_manager.users.models import User

USERNAME_FIELD_SESCRIPTION = _("Обязательное поле. "
                               "Не более 150 символов. "
                               "Только буквы, цифры и символы @/./+/-/_.")
PASSWORD_REQUIREMENTS_MESSAGE = _("Ваш пароль должен содержать как минимум 3 символа.")
REPEAT_PASSWORD_MESSAGE = _("Для подтверждения введите, пожалуйста, пароль ещё раз.")
SHORT_PASSWORD_ERROR = _("Введённый пароль слишком короткий. "
                         "Он должен содержать как минимум 3 символа.")


class RegisterUserForm(UserCreationForm):

    def __init__(self, *args, **kwargs):
        is_update = kwargs.pop('is_update', False)
        super().__init__(*args, **kwargs)
        as_ul = format_html("<ul>{}</ul>",
                            format_html("<li>{}</li>",
                                        PASSWORD_REQUIREMENTS_MESSAGE))
        self.fields["password1"].help_text = as_ul
        self.fields["password2"].help_text = REPEAT_PASSWORD_MESSAGE

        if is_update:
            self.fields['username'].required = False  # Делаем поле необязательным
            self.fields['password1'].required = False  # Пароль можно не менять при обновлении
            self.fields['password2'].required = False  # Повторный пароль тоже не обязателен

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
                                    attrs={'class': 'form-input'}),
                                ),

    password2 = forms.CharField(label=_('Repeat Password'),
                                error_messages={"required": SHORT_PASSWORD_ERROR},
                                required=True,
                                widget=forms.PasswordInput(attrs={'class': 'form-input'}))

    class Meta:
        model = get_user_model()
        fields = ['first_name', 'last_name', 'username', 'password1', 'password2']
