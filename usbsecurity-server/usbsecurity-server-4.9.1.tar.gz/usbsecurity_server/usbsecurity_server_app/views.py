import os

import django.contrib.auth as auth
from django.conf.global_settings import LANGUAGE_COOKIE_NAME
from django.contrib.auth.mixins import LoginRequiredMixin
from django.http import JsonResponse, Http404, FileResponse

from django.shortcuts import redirect
from django.urls import reverse
from django.utils import translation
from django.utils.decorators import method_decorator
from django.views.decorators.csrf import csrf_protect
from django.views.defaults import page_not_found
from django.views.generic import TemplateView

from usbsecurity_server.usbsecurity_server.settings import ACTION_ADD, ACTION_REMOVE, BASE_DIR
from usbsecurity_server.usbsecurity_server_app.exceptions import UserDoesNotExist, AuthenticationError, \
    IncorrectPassword, PasswordsNotMatch
from usbsecurity_server.usbsecurity_server_app.forms import LoginForm, PasswordForm, AppearanceForm, LanguageForm
from usbsecurity_server.usbsecurity_server_app.mixins import CheckLoginMixin, AccountPersonalRequiredMixin, \
    LanguageCheckMixin, AccountRequiredMixin
from usbsecurity_server.usbsecurity_server_app.models import AccountSession, Computer, AccountComputer, Device, \
    AccountDevice


def page_not_found_404(request, exception):
    return page_not_found(request, exception, template_name='admin/404.html')


class ActionDeviceView(TemplateView):
    def get(self, request, *args, **kwargs):
        action = kwargs.get('action')
        device_id = kwargs.get('device_id')

        data = {
            'error': None,
            'is_authorized': False
        }

        if action == ACTION_ADD:
            opened_sessions = AccountSession.objects.opened_sessions(ip_address=request.META['REMOTE_ADDR'])
            if not opened_sessions.exists():
                data['error'] = 'No session is open on the computer'
                return JsonResponse(data, safe=False)

            try:
                computer = Computer.objects.get_computer(request.META['REMOTE_ADDR'])
            except Computer.DoesNotExist:
                computer = None

            if computer:
                opened_sessions_accounts = opened_sessions.values_list('account', flat=True)
                ac_computers = AccountComputer.objects.all_computers(opened_sessions_accounts)
                if ac_computers.exists():
                    try:
                        ac_computers.get_assoc(computer)
                    except AccountComputer.DoesNotExist:
                        data['error'] = 'User not associated with the computer'
                        return JsonResponse(data, safe=False)

            try:
                device = Device.objects.get_device(device_id)
            except Device.DoesNotExist:
                device = None

            if device:
                opened_sessions_accounts = opened_sessions.values_list('account', flat=True)
                ac_devices = AccountDevice.objects.all_devices(opened_sessions_accounts)
                if ac_devices.exists():
                    try:
                        ac_devices.get_assoc(device)
                    except AccountDevice.DoesNotExist:
                        data['error'] = 'User not associated with the device'
                        return JsonResponse(data, safe=False)

            data['is_authorized'] = True
            return JsonResponse(data, safe=False)
        if action == ACTION_REMOVE:
            ip_address = request.META['REMOTE_ADDR']
            AccountSession.objects.close_sessions(ip_address)
            opened_sessions = AccountSession.objects.opened_sessions(ip_address=ip_address)
            data['is_authorized'] = opened_sessions.exists()
            return JsonResponse(data, safe=False)
        else:
            data['error'] = 'Undefined action'
            return JsonResponse(data, safe=False)


# class DownloadManualView(TemplateView):
#     def get(self, request, *args, **kwargs):
#         response = HttpResponse(content_type='application/pdf')
#         response['Content-Disposition'] = "attachment; filename=%s" % smart_str('manual_protocolo.pdf')
#         response['X-Sendfile'] = os.path.join(BASE_DIR, 'static', 'doc', 'manual_es.pdf')
#         return response


class UserManualView(TemplateView):
    def get(self, request, *args, **kwargs):
        lang = translation.get_language()

        file = open(os.path.join(BASE_DIR, 'static', 'doc', 'manual', 'user', 'manual_en.pdf'), 'rb')
        if lang == 'es':
            file = open(os.path.join(BASE_DIR, 'static', 'doc', 'manual', 'user', 'manual_es.pdf'), 'rb')

        try:
            return FileResponse(file, content_type='application/pdf')
        except FileNotFoundError:
            raise Http404()


class BaseView(TemplateView):
    def get_context_data(self, **kwargs):
        context = super(BaseView, self).get_context_data()
        
        about = {}
        with open(os.path.join(BASE_DIR, '__version__.py')) as f:
            exec(f.read(), about)
            
        context['version'] = about['__version__']            
        return context


class HomeView(CheckLoginMixin, BaseView):
    template_name = 'index.html'


class LoginView(CheckLoginMixin, BaseView):
    template_name = 'login.html'

    def get(self, request, *args, **kwargs):
        context = self.get_context_data(**kwargs)
        context['form'] = LoginForm()
        return self.render_to_response(context)

    @method_decorator(csrf_protect)
    def post(self, request, *args, **kwargs):
        context = self.get_context_data(**kwargs)

        form = LoginForm(request.POST)
        if not form.is_valid():
            context['form'] = form
            return self.render_to_response(context)

        try:
            user = form.save()

            if not user.is_active:
                return self.render_to_response(context)

            auth.login(request, user)
            if not user.is_authenticated:
                return redirect(reverse('login'))

            ip_address = request.META['REMOTE_ADDR']
            AccountSession.objects.close_sessions(ip_address)
            AccountSession.objects.create_session(user.account, ip_address)

            next_page = request.GET.get('next', None)
            if not next_page:
                return redirect(reverse('account'))
            return redirect(next_page)
        except (UserDoesNotExist, AuthenticationError, IncorrectPassword):
            context['form'] = form
            return self.render_to_response(context)


class SettingsAppearanceView(CheckLoginMixin, LanguageCheckMixin, BaseView):
    template_name = 'settings/appearance.html'

    def get(self, request, *args, **kwargs):
        context = self.get_context_data(**kwargs)
        context['form'] = AppearanceForm(appearance=request.session.get('appearance'))
        return self.render_to_response(context)

    @method_decorator(csrf_protect)
    def post(self, request, *args, **kwargs):
        form = AppearanceForm(request.POST, appearance=request.session.get('appearance'))
        if not form.is_valid():
            raise Http404()

        form.save(request)
        return redirect(request.path)


class SettingsLanguageView(CheckLoginMixin, LanguageCheckMixin, BaseView):
    template_name = 'settings/language.html'

    def get(self, request, *args, **kwargs):
        context = self.get_context_data(**kwargs)
        context['form'] = LanguageForm()
        return self.render_to_response(context)

    @method_decorator(csrf_protect)
    def post(self, request, *args, **kwargs):
        form = LanguageForm(request.POST)
        if not form.is_valid():
            raise Http404()

        code, _next = form.save(request)
        request.session['language_code'] = code

        response = redirect(request.path if not _next else _next)
        response.set_cookie(LANGUAGE_COOKIE_NAME, code)
        return response


class HelpAboutView(CheckLoginMixin, LanguageCheckMixin, BaseView):
    template_name = 'help/about.html'


class HelpAuthorView(CheckLoginMixin, LanguageCheckMixin, BaseView):
    template_name = 'help/author.html'


class HelpTranslationView(CheckLoginMixin, LanguageCheckMixin, BaseView):
    template_name = 'help/translation.html'


class AccountView(CheckLoginMixin, LoginRequiredMixin, AccountRequiredMixin, LanguageCheckMixin, BaseView):
    template_name = 'account.html'

    def get(self, request, *args, **kwargs):
        context = self.get_context_data(**kwargs)

        if not request.user.account.is_for_all:
            context['ac_devices'] = AccountDevice.objects.all_devices(request.user.account)

        return self.render_to_response(context)


class AccountLogoutView(CheckLoginMixin, LoginRequiredMixin, LanguageCheckMixin, BaseView):
    template_name = 'account/logout.html'

    @method_decorator(csrf_protect)
    def post(self, request, *args, **kwargs):
        AccountSession.objects.close_sessions(request.META['REMOTE_ADDR'])
        auth.logout(request)
        return redirect(reverse('login'))


class AccountPasswordView(CheckLoginMixin, LoginRequiredMixin, AccountRequiredMixin, LanguageCheckMixin,
                          AccountPersonalRequiredMixin, BaseView):
    template_name = 'account/password.html'

    def get(self, request, *args, **kwargs):
        context = self.get_context_data(**kwargs)
        context['form'] = PasswordForm()
        return self.render_to_response(context)

    @method_decorator(csrf_protect)
    def post(self, request, *args, **kwargs):
        context = self.get_context_data(**kwargs)

        form = PasswordForm(request.POST)
        if not form.is_valid():
            context['form'] = form
            return self.render_to_response(context)

        try:
            form.save(request.user)
            return redirect(reverse('login'))
        except (IncorrectPassword, PasswordsNotMatch):
            context['form'] = form
            return self.render_to_response(context)
