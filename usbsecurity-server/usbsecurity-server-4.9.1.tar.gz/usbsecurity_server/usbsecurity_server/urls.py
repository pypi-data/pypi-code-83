"""usbsecurity_server URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
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

from django.conf.urls.i18n import i18n_patterns
from django.contrib import admin
from django.urls import path
from django.views.i18n import JavaScriptCatalog

from usbsecurity_server.usbsecurity_server_app.ajax import geocode
from usbsecurity_server.usbsecurity_server_app.views import HomeView, LoginView, AccountView, AccountLogoutView, AccountPasswordView, \
    ActionDeviceView, SettingsAppearanceView, SettingsLanguageView, HelpAboutView, HelpAuthorView, HelpTranslationView, \
    page_not_found_404, UserManualView

handler404 = page_not_found_404


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', HomeView.as_view(), name='home'),
    # Doc
    path('manual/user/', UserManualView.as_view(), name='user_manual'),
    path('login/', LoginView.as_view(), name='login'),
    path('account/', AccountView.as_view(), name='account'),
    path('account/logout/', AccountLogoutView.as_view(), name='account_logout'),
    path('account/passsword/', AccountPasswordView.as_view(), name='account_password'),
    # Settings
    path('settings/appearance/', SettingsAppearanceView.as_view(), name='settings_appearance'),
    path('settings/language/', SettingsLanguageView.as_view(), name='settings_language'),
    # Help
    path('help/about/', HelpAboutView.as_view(), name='help_about'),
    path('help/author/', HelpAuthorView.as_view(), name='help_author'),
    path('help/translation/', HelpTranslationView.as_view(), name='help_translation'),
    # Api
    path('api/action/<str:action>/<str:device_id>/', ActionDeviceView.as_view(), name='url_api'),
    # Ajax
    path('ajax/geocode/', geocode),
]

urlpatterns += i18n_patterns(
    path('jsi18n/', JavaScriptCatalog.as_view(), name='javascript-catalog'),
)
