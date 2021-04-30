from django.conf.urls import include, url
from django.utils.translation import gettext_lazy as _

from wagtail.admin.menu import Menu, SubmenuMenuItem
from wagtail.core import hooks

from wagtaildonate import admin_urls
from wagtaildonate.settings import donate_settings


def register_admin_urls():
    return [url(r"^donate/", include(admin_urls, namespace="wagtaildonate_admin"))]


class PaymentsMenu(SubmenuMenuItem):
    def is_shown(self, request):
        payment_perms = [
            "wagtaildonate.can_export_donations",
            "wagtaildonate.can_export_recurring_donations",
        ]
        return any(request.user.has_perm(perm) for perm in payment_perms)


def register_payments_menu():
    return PaymentsMenu(
        _("Payments"),
        Menu(register_hook_name="register_payments_menu_item"),
        classnames="icon icon-cogs",
    )


def register_general_wagtail_hooks():
    if donate_settings.DONATION_EXPORT_ENABLED:
        hooks.register("register_admin_urls", register_admin_urls)
        hooks.register("register_admin_menu_item", register_payments_menu)
