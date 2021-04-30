import datetime

from django.contrib.auth.mixins import PermissionRequiredMixin
from django.utils.translation import gettext as _
from django.views.generic import FormView

from wagtail.admin.views.reports import SpreadsheetExportMixin

from wagtaildonate.admin_forms import DateRangeForm
from wagtaildonate.models.utils import (
    get_donation_export_log_model,
    get_pay_in_model,
    get_recurring_donation_model,
    get_single_donation_model,
)


class BaseExportView(SpreadsheetExportMixin, FormView):
    template_name = "wagtaildonate/admin/export_view.html"
    donation_model = None
    export_log_model = get_donation_export_log_model()
    form_class = DateRangeForm
    log_donation_type = ""
    title = _("Export donations")

    def get_donation_model(self):
        return self.donation_model

    def get_queryset(self):
        return self.get_donation_model().objects.all()

    def get_export_log_model(self):
        return self.export_log_model

    def get_log_donation_type(self):
        return self.log_donation_type

    def get_user_information(self):
        model = self.get_export_log_model()
        remote_addr_max_length = model._meta.get_field("remote_addr").max_length
        remote_host_max_length = model._meta.get_field("remote_host").max_length
        user_name_max_length = model._meta.get_field("user_name").max_length
        x_forwarded_for_max_length = model._meta.get_field("x_forwarded_for").max_length
        user_agent_max_length = model._meta.get_field("user_agent").max_length
        remote_host = self.request.META.get("REMOTE_HOST", "")[:remote_host_max_length]
        remote_addr = self.request.META.get("REMOTE_ADDR", "")[:remote_addr_max_length]
        x_forwarded_for = self.request.META.get("HTTP_X_FORWARDED_FOR", "")[
            :x_forwarded_for_max_length
        ]
        user_agent = self.request.META.get("HTTP_USER_AGENT", "")[
            :user_agent_max_length
        ]
        user_name = self.request.user.get_username()[:user_name_max_length]
        return {
            "remote_addr": remote_addr,
            "remote_host": remote_host,
            "x_forwarded_for": x_forwarded_for,
            "user_agent": user_agent,
            "user": self.request.user,
            "user_name": user_name,
        }

    def form_valid(self, form):
        from_date = form.cleaned_data["from_date"]
        to_date = form.cleaned_data["to_date"]

        model = self.get_export_log_model()

        # Log
        model.objects.create(
            donation_type=self.get_log_donation_type(),
            datetime_from=from_date,
            datetime_to=to_date,
            **self.get_user_information(),
        )

        donations = self.get_queryset()

        if from_date:
            donations = donations.filter(created_at__date__gte=from_date)

        if to_date:
            donations = donations.filter(created_at__date__lte=to_date)

        return self.as_spreadsheet(donations, self.request.POST.get("format", "csv"))

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["title"] = self.title
        return context


class DonationExportView(PermissionRequiredMixin, BaseExportView):
    donation_model = get_single_donation_model()
    list_export = [
        "created_at",
        "payment_method",
        "transaction_id",
        "get_transaction_status_display",
        "provider_transaction_status",
        "amount",
        "first_name",
        "surname",
        "email",
        "phone_number",
        "address_line_1",
        "address_line_2",
        "address_line_3",
        "town",
        "postal_code",
        "country",
        "on_behalf_of_organisation",
        "gift_aid_declaration",
        "in_memory",
        "in_memory_of",
        "sms_consent",
        "phone_consent",
        "email_consent",
        "post_consent",
        "donation_page_id",
    ]
    export_headings = {
        "payment_method": "Provider",
        "donation_page_id": "Donation Page",
        "get_transaction_status_display": "Transaction Status",
        "sms_consent": "SMS Consent",
    }
    log_donation_type = get_donation_export_log_model().DONATION_TYPE_SINGLE
    permission_required = "wagtaildonate.can_export_donations"

    def get_filename(self):
        return "single-donations-export-" + datetime.date.today().isoformat()


class RecurringDonationExportView(PermissionRequiredMixin, BaseExportView):
    donation_model = get_recurring_donation_model()
    list_export = [
        "created_at",
        "payment_method",
        "subscription_id",
        "amount",
        "get_frequency_display",
        "first_name",
        "surname",
        "email",
        "phone_number",
        "address_line_1",
        "address_line_2",
        "address_line_3",
        "town",
        "postal_code",
        "country",
        "on_behalf_of_organisation",
        "gift_aid_declaration",
        "in_memory",
        "in_memory_of",
        "sms_consent",
        "phone_consent",
        "email_consent",
        "post_consent",
        "donation_page_id",
    ]
    export_headings = {
        "payment_method": "Provider",
        "get_frequency_display": "Frequency",
        "sms_consent": "SMS Consent",
        "donation_page_id": "Donation Page",
    }
    log_donation_type = get_donation_export_log_model().DONATION_TYPE_RECURRING
    permission_required = "wagtaildonate.can_export_recurring_donations"
    title = _("Export recurring donations")

    def get_filename(self):
        return "recurring-donations-export-" + datetime.date.today().isoformat()


class PayInExportView(PermissionRequiredMixin, BaseExportView):
    donation_model = get_pay_in_model()
    list_export = [
        "created_at",
        "payment_method",
        "transaction_id",
        "get_transaction_status_display",
        "provider_transaction_status",
        "amount",
        "first_name",
        "surname",
        "email",
        "phone_number",
        "address_line_1",
        "address_line_2",
        "address_line_3",
        "town",
        "postal_code",
        "country",
        "on_behalf_of_organisation",
        "in_memory",
        "in_memory_of",
        "sms_consent",
        "phone_consent",
        "email_consent",
        "post_consent",
        "donation_page_id",
        "event_name",
        "event_code",
        "fundraiser_reference",
    ]
    export_headings = {
        "payment_method": "Provider",
        "donation_page_id": "Donation Page",
        "get_transaction_status_display": "Transaction Status",
        "sms_consent": "SMS Consent",
    }
    log_donation_type = get_donation_export_log_model().DONATION_TYPE_PAY_IN
    permission_required = "wagtaildonate.can_export_pay_ins"

    def get_filename(self):
        return "pay-ins-export-" + datetime.date.today().isoformat()
