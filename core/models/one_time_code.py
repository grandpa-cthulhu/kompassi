import logging
from random import choice

from django.conf import settings
from django.db import models
from django.utils import timezone
from django.utils.translation import gettext_lazy as _

from .constants import EMAIL_LENGTH


logger = logging.getLogger("kompassi")


ONE_TIME_CODE_LENGTH = 40
ONE_TIME_CODE_ALPHABET = "0123456789abcdef"
ONE_TIME_CODE_STATE_CHOICES = [
    ("valid", _("Valid")),
    ("used", _("Used")),
    ("revoked", _("Revoked")),
]


class OneTimeCodeMixin:
    @property
    def is_used(self):
        return self.used_at is not None

    @property
    def from_email(self):
        return settings.DEFAULT_FROM_EMAIL

    def __str__(self):
        return self.code

    def revoke(self):
        assert self.state == "valid"
        self.state = "revoked"
        self.used_at = timezone.now()
        self.save()

    def render_message_subject(self, request):
        raise NotImplemented()

    def render_message_body(self, request):
        raise NotImplemented()

    def send(self, request, **kwargs):
        body = self.render_message_body(request)
        subject = self.render_message_subject(request)

        opts = dict(
            subject=subject,
            body=body,
            from_email=self.from_email,
            to=(self.name_and_email,),
        )

        opts.update(kwargs)

        if "background_tasks" in settings.INSTALLED_APPS:
            from ..tasks import send_email

            send_email.delay(**opts)
        else:
            from django.core.mail import EmailMessage

            if settings.DEBUG:
                logger.debug(body)

            EmailMessage(**opts).send(fail_silently=True)

    def mark_used(self):
        assert self.state == "valid"

        self.used_at = timezone.now()
        self.state = "used"
        self.save()

    @classmethod
    def generate_code(cls):
        return "".join(choice(ONE_TIME_CODE_ALPHABET) for _ in range(ONE_TIME_CODE_LENGTH))


class OneTimeCode(models.Model, OneTimeCodeMixin):
    code = models.CharField(max_length=63, unique=True)
    person = models.ForeignKey("core.Person", on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    used_at = models.DateTimeField(null=True, blank=True)
    state = models.CharField(
        max_length=8,
        default="valid",
        choices=ONE_TIME_CODE_STATE_CHOICES,
    )

    def save(self, *args, **kwargs):
        if not self.code:
            self.code = "".join(choice(ONE_TIME_CODE_ALPHABET) for _ in range(ONE_TIME_CODE_LENGTH))

        return super().save(*args, **kwargs)

    @property
    def name_and_email(self):
        return self.person.name_and_email

    class Meta:
        abstract = True
        index_together = [
            ("person", "state"),
        ]


class OneTimeCodeLite(models.Model, OneTimeCodeMixin):
    """
    An OneTimeCode that is not tied to a Person.
    """

    code = models.CharField(max_length=63, unique=True)
    email = models.EmailField(
        blank=True,
        max_length=EMAIL_LENGTH,
        verbose_name=_("E-mail address"),
    )
    created_at = models.DateTimeField(auto_now_add=True)
    used_at = models.DateTimeField(null=True, blank=True)
    state = models.CharField(
        max_length=8,
        default="valid",
        choices=ONE_TIME_CODE_STATE_CHOICES,
    )

    def save(self, *args, **kwargs):
        if not self.code:
            self.code = self.generate_code()

        return super().save(*args, **kwargs)

    @property
    def name_and_email(self):
        return self.email

    class Meta:
        abstract = True
        index_together = [
            ("email", "state"),
        ]
