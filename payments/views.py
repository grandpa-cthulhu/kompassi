import logging

from django.http import HttpResponseRedirect, HttpResponseNotAllowed, HttpResponse
from django.conf import settings
from django.contrib import messages
from django.core.exceptions import ValidationError
from django.shortcuts import redirect, render
from django.utils.translation import gettext_lazy as _
from django.views.decorators.http import require_GET

from csp.decorators import csp_update
from core.utils import url

from .helpers import valid_signature_required


logger = logging.getLogger("kompassi")


@valid_signature_required
def payments_checkout_success_view(request, payment):
    """
    https://checkoutfinland.github.io/psp-api/#/?id=redirect-and-callback-url-parameters
    """
    payment.process_checkout_response(request.GET)

    if payment.status == "ok":
        messages.success(request, _("Payment successful. Thank you for your order!"))
    elif payment.status in ["pending", "delayed"]:
        messages.warning(
            request,
            _(
                "The order was successful, but we are still waiting for final confirmation of payment from the payment processor. "
                "You will receive your e-tickets once we have received the confirmation. This may take up to three banking days."
            ),
        )
    else:
        logger.warn(
            "Success callback called with non-successful status %s. This should not happen idk?", payment.status
        )
        messages.error(request, _("The payment was not completed. Please try again."))

    return payment.get_redirect()


@valid_signature_required
def payments_checkout_cancel_view(request, payment):
    payment.process_checkout_response(request.GET)

    messages.error(request, _("The payment was not completed. Please try again."))
    return payment.get_redirect()


@valid_signature_required
def payments_checkout_success_callback(request, payment):
    payment.process_checkout_response(request.GET)
    return HttpResponse("")


@valid_signature_required
def payments_checkout_cancel_callback(request, payment):
    payment.process_checkout_response(request.GET)
    return HttpResponse("")
