#  This module belongs to the usbsecurity-server project.
#  Copyright (c) 2021 Alexis Torres Valdes
#
#  This program is free software: you can redistribute it and/or modify
#  it under the terms of the GNU Affero General Public License as published
#  by the Free Software Foundation, either version 3 of the License, or
#   (at your option) any later version.
#
#  This program is distributed in the hope that it will be useful,
#  but WITHOUT ANY WARRANTY; without even the implied warranty of
#  MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#  GNU Affero General Public License for more details.
#
#  You should have received a copy of the GNU Affero General Public License
#  along with this program.  If not, see <https://www.gnu.org/licenses/>.
#
#  Contact: alexis89.dev@gmail.com

import django.forms as forms
import django.contrib.auth as auth
from django.utils import translation

from django.utils.translation import gettext_lazy as _
from django.contrib.auth.models import User
from django.core.validators import RegexValidator

from usbsecurity_server.usbsecurity_server.settings import LANGUAGES
from usbsecurity_server.usbsecurity_server_app.exceptions import IncorrectPassword, UserDisabled, AuthenticationError, UserDoesNotExist, \
    PasswordsNotMatch
from usbsecurity_server.usbsecurity_server_app.models import Device, Account
from usbsecurity_server.usbsecurity_server_app.utils import set_language


class AppearanceForm(forms.Form):
    CHOICES = (
        ('auto', _('Light/Dark')),
        ('light', _('Light')),
        ('dark', _('Dark')),
    )

    def __init__(self, *args, **kwargs):
        appearance = kwargs.pop('appearance')
        super(AppearanceForm, self).__init__(*args, **kwargs)
        self.fields['mode'] = forms.ChoiceField(choices=self.CHOICES,
                                                widget=forms.RadioSelect(
                                                    attrs={'class': 'is-checkradio'}))
        if appearance == 'light':
            self.fields['mode'].initial = self.CHOICES[1]
        elif appearance == 'dark':
            self.fields['mode'].initial = self.CHOICES[2]
        else:
            self.fields['mode'].initial = self.CHOICES[0]

    def save(self, request):
        mode = self.cleaned_data['mode']
        request.session['appearance'] = mode


class LanguageForm(forms.Form):
    def __init__(self, *args, **kwargs):
        super(LanguageForm, self).__init__(*args, **kwargs)
        self.fields['code'] = forms.ChoiceField(choices=LANGUAGES,
                                                widget=forms.RadioSelect(
                                                    attrs={'class': 'is-checkradio'}))
        lang = translation.get_language()
        if lang == 'es':
            self.fields['code'].initial = LANGUAGES[1]
        else:
            self.fields['code'].initial = LANGUAGES[0]

    next = forms.CharField(required=False, widget=forms.HiddenInput())

    def save(self, request):
        code = self.cleaned_data['code']
        _next = self.cleaned_data['next']

        if request.user.is_authenticated:
            try:
                account = Account.objects.get_account(request.user)
                set_language(account, code)
            except Account.DoesNotExist:
                pass

        request.session['language_code'] = code
        return code, _next


class DeviceAdminForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super(DeviceAdminForm, self).__init__(*args, **kwargs)
        self.fields['ls_id'] = forms.CharField(label='Linux ID',
                                               max_length=9,
                                               required=True,
                                               validators=[
                                                   RegexValidator(
                                                       regex='^[a-fA-F0-9]{4}:[a-fA-F0-9]{4}$',
                                                       message=_('Incorrect value. The format should be "xxxx:xxxx", where x can take the following values: 0-9|a-f|A-F'),
                                                   ),
                                               ],
                                               help_text=_('Obtained by executing "lsusb".'))

    class Meta:
        model = Device
        fields = '__all__'


class LoginForm(forms.Form):
    username = forms.CharField(required=True,
                               widget=forms.TextInput(
                                   attrs={'class': 'input', 'placeholder': _('Enter your username')}))
    password = forms.CharField(required=True,
                               max_length=255,
                               widget=forms.PasswordInput(
                                   attrs={'class': 'input', 'placeholder': _('Enter your password')}))

    def save(self):
        username = self.cleaned_data['username']
        password = self.cleaned_data['password']

        try:
            user = User.objects.get_by_natural_key(username)

            try:
                Account.objects.get_account(user)
            except Account.DoesNotExist:
                self.add_error('username', _('No account exists for this user'))
                raise IncorrectPassword

            if not user.check_password(password):
                self.add_error('password', _('Incorrect password'))
                raise IncorrectPassword

            if not user.is_active:
                self.add_error('username', _('Inactive user. Contact your administrator'))
                raise UserDisabled

            user = auth.authenticate(username=username, password=password)
            if not user:
                self.add_error('username', _('Authentication error'))
                raise AuthenticationError

            return user
        except User.DoesNotExist:
            self.add_error('username', _('There is no user with this name'))
            raise UserDoesNotExist


class PasswordForm(forms.Form):
    password = forms.CharField(required=True,
                               min_length=6,
                               max_length=255,
                               widget=forms.PasswordInput(attrs={'class': 'input',
                                                                 'placeholder': _('Enter your current password')}))
    new_password = forms.CharField(required=True,
                                   min_length=6,
                                   max_length=255,
                                   widget=forms.PasswordInput(attrs={'class': 'input',
                                                                     'placeholder': _('Enter your new password')}))
    confirm_new_password = forms.CharField(required=True,
                                           min_length=6,
                                           max_length=255,
                                           widget=forms.PasswordInput(attrs={'class': 'input',
                                                                             'placeholder': _('Confirm your new password')}))

    def save(self, user):
        password = self.cleaned_data['password']
        new_password = self.cleaned_data['new_password']
        confirm_new_password = self.cleaned_data['confirm_new_password']

        if not user.check_password(password):
            self.add_error('password', _('Incorrect password'))
            raise IncorrectPassword

        if new_password != confirm_new_password:
            msg = _('Passwords do not match')
            self.add_error('new_password', msg)
            self.add_error('confirm_new_password', msg)
            raise PasswordsNotMatch

        user.set_password(new_password)

        user = user.save()
        return user
