# encoding: utf-8

from datetime import date, datetime, timedelta

from django.conf import settings
from django.contrib.auth.models import User
from django.db import models
from django.template import RequestContext
from django.template.loader import render_to_string
from django.utils.dateformat import format as format_date
from django.utils import timezone

from .utils import validate_slug, SLUG_FIELD_PARAMS, url


class Venue(models.Model):
    name = models.CharField(max_length=63, verbose_name=u'Tapahtumapaikan nimi')
    name_inessive = models.CharField(
        max_length=63,
        verbose_name=u'Tapahtumapaikan nimi inessiivissä',
        help_text=u'Esimerkki: Paasitornissa',
    )

    class Meta:
        verbose_name = u'Tapahtumapaikka'
        verbose_name_plural = u'Tapahtumapaikat'

    def __unicode__(self):
        return self.name

    def save(self, *args, **kwargs):
        if self.name and not self.name_inessive:
            self.name_inessive = self.name + 'ssa'

        return super(Venue, self).save(*args, **kwargs)

    @classmethod
    def create_dummy(cls):
        return cls.objects.create(
            name='Dummy venue'
        )


class Event(models.Model):
    slug = models.CharField(**SLUG_FIELD_PARAMS)
    name = models.CharField(max_length=63, verbose_name=u'Tapahtuman nimi')

    name_genitive = models.CharField(
        max_length=63,
        verbose_name=u'Tapahtuman nimi genetiivissä',
        help_text=u'Esimerkki: Susiconin',
    )

    name_illative = models.CharField(
        max_length=63,
        verbose_name=u'Tapahtuman nimi illatiivissä',
        help_text=u'Esimerkki: Susiconiin',
    )

    name_inessive = models.CharField(
        max_length=63,
        verbose_name=u'Tapahtuman nimi inessiivissä',
        help_text=u'Esimerkki: Susiconissa',
    )

    description = models.TextField(blank=True, verbose_name=u'Kuvaus')

    venue = models.ForeignKey(Venue,
        verbose_name=u'Tapahtumapaikka',
    )

    start_time = models.DateTimeField(
        null=True,
        blank=True,
        verbose_name=u'Alkamisaika',
    )

    end_time = models.DateTimeField(
        null=True,
        blank=True,
        verbose_name=u'Päättymisaika',
    )

    homepage_url = models.CharField(
        blank=True,
        max_length=255,
        verbose_name=u'Tapahtuman kotisivu',
    )

    organization_name = models.CharField(
        blank=True,
        max_length=63,
        verbose_name=u'Järjestävä taho',
    )

    organization_url = models.CharField(
        blank=True,
        max_length=255,
        verbose_name=u'Järjestävän tahon kotisivu'
    )

    public = models.BooleanField(
        default=True,
        verbose_name=u'Julkinen',
        help_text=u'Julkiset tapahtumat näytetään etusivulla.'
    )

    class Meta:
        verbose_name = u'Tapahtuma'
        verbose_name_plural = u'Tapahtumat'

    def __unicode__(self):
        return self.name

    def save(self, *args, **kwargs):
        if self.name:
            for field, suffix in [
                ('name_genitive', 'in'),
                ('name_illative', 'iin'),
                ('name_inessive', 'issa'),
            ]:
                if not getattr(self, field, None):
                    setattr(self, field, self.name + suffix)

        return super(Event, self).save(*args, **kwargs)

    @property
    def name_and_year(self):
        return u"{name} ({year})".format(
            name=self.name,
            year=self.start_time.year,
        )

    @classmethod
    def get_or_create_dummy(cls):
        venue = Venue.create_dummy()
        t = timezone.now()

        return cls.objects.get_or_create(
            name='Dummy event',
            defaults=dict(
                venue=venue,
                start_time=t + timedelta(days=60),
                end_time=t + timedelta(days=61),
                slug='dummy',
            ),
        )

    # XXX BEGIN UGLY COPYPASTA
    @property
    def labour_event_meta(self):
        if 'labour' not in settings.INSTALLED_APPS:
            return None

        from labour.models import LabourEventMeta

        try:
            return self.laboureventmeta
        except LabourEventMeta.DoesNotExist:
            return None

    @property
    def programme_event_meta(self):
        if 'programme' not in settings.INSTALLED_APPS:
            return None

        from programme.models import ProgrammeEventMeta

        try:
            return self.programmeeventmeta
        except ProgrammeEventMeta.DoesNotExist:
            return None

    def app_event_meta(self, app_label):
        return getattr(self, '{}_event_meta'.format(app_label))

    @property
    def badges_event_meta(self):
        if 'badges' not in settings.INSTALLED_APPS:
            return None

        from badges.models import BadgesEventMeta

        try:
            return self.badgeseventmeta
        except BadgesEventMeta.DoesNotExist:
            return None

    @property
    def tickets_event_meta(self):
        if 'tickets' not in settings.INSTALLED_APPS:
            return None

        from tickets.models import TicketsEventMeta

        try:
            return self.ticketseventmeta
        except TicketsEventMeta.DoesNotExist:
            return None
    # XXX END UGLY COPYPASTA


EMAIL_LENGTH = PHONE_NUMBER_LENGTH = 255
BIRTH_DATE_HELP_TEXT = u'Syntymäaika muodossa {0}'.format(
    format_date(date(1994, 2, 24), settings.DATE_FORMAT)
)


class Person(models.Model):
    first_name = models.CharField(max_length=1023, verbose_name=u'Etunimi')
    surname = models.CharField(max_length=1023, verbose_name=u'Sukunimi')
    nick = models.CharField(blank=True, max_length=1023, help_text='Lempi- tai kutsumanimi')
    birth_date = models.DateField(
        null=True,
        blank=True,
        verbose_name=u'Syntymäaika',
        help_text=BIRTH_DATE_HELP_TEXT)

    email = models.EmailField(
        blank=True,
        max_length=EMAIL_LENGTH,
        verbose_name=u'Sähköpostiosoite'
    )

    phone = models.CharField(
        blank=True,
        max_length=PHONE_NUMBER_LENGTH,
        verbose_name=u'Puhelinnumero'
    )

    anonymous = models.BooleanField(
        default=False,
        verbose_name=u'Piilota etu- ja sukunimi',
        help_text=u'Jos valitset tämän, sinusta näytetään vain nick-kentässä asetettu '
            u'kutsumanimi. Etu- ja sukunimi on tällöinkin annettava, jolloin ne näkyvät '
            u'vain tapahtuman järjestäjille.'
    )

    may_send_info = models.BooleanField(
        default=False,
        verbose_name=u'Minulle saa lähettää sähköpostitse tietoa tulevista tapahtumista <i>(vapaaehtoinen)</i>',
    )

    notes = models.TextField(blank=True, verbose_name=u'Käsittelijän merkinnät')
    user = models.OneToOneField('auth.User', null=True, blank=True)

    email_verified_at = models.DateTimeField(null=True, blank=True)

    class Meta:
        ordering = ['surname']
        verbose_name = u'Henkilö'
        verbose_name_plural = u'Henkilöt'

    def __unicode__(self):
        return self.full_name

    def clean(self):
        if self.anonymous and not self.nick:
            from django.core.exceptions import ValidationError
            raise ValidationError(u'Jos oikea nimi piilotetaan, nick täytyy antaa.')

    @property
    def full_name(self):
        if self.nick:
            return u'{0} "{1}" {2}'.format(
                self.first_name,
                self.nick,
                self.surname
            )
        else:
            return u'{0} {1}'.format(
                self.first_name,
                self.surname
            )

    @property
    def name_and_email(self):
        return u"{self.first_name} {self.surname} <{self.email}>".format(self=self)

    @property
    def display_name(self):
        if self.anonymous:
            return self.nick
        else:
            return self.full_name

    @classmethod
    def get_or_create_dummy(cls, superuser=True):
        user, unused = User.objects.get_or_create(
            username='mahti',
            defaults=dict(
                first_name='Markku',
                last_name='Mahtinen',
                is_staff=superuser,
                is_superuser=superuser,
            ),
        )

        if not user.password:
            user.set_password('mahti')
            user.save()

        return cls.objects.get_or_create(
            user=user,
            defaults=dict(
                first_name=user.first_name,
                surname=user.last_name,
                nick='Mahti',
                birth_date=date(1984, 1, 1),
                email='mahti@example.com',
                phone='+358 50 555 1234'
            )
        )

    def save(self, *args, **kwargs):
        ret_val = super(Person, self).save(*args, **kwargs)

        if self.user:
            # Update first_name, last_name and email in User if they differ from those in Person
            for person_attr, user_attr in [
                ('first_name', 'first_name'),
                ('surname', 'last_name'),
                ('email', 'email'),
            ]:
                setattr(self.user, user_attr, getattr(self, person_attr))

            self.user.save()

        return ret_val

    @property
    def is_email_verified(self):
        return self.email_verified_at is not None

    @property
    def pending_email_verification(self):
        try:
            return EmailVerificationToken.objects.get(person=self, state='valid')
        except EmailVerificationToken.DoesNotExist:
            return None

    @property
    def is_email_verification_pending(self):
        return self.pending_email_verification is not None

    def setup_email_verification(self, request):
        self.email_verified_at = None
        self.save()

        pending_verification = self.pending_email_verification
        if pending_verification:
            pending_verification.revoke()

        code = EmailVerificationToken(person=self)
        code.save()
        code.send(request)

    def verify_email(self, code):
        try:
            code = EmailVerificationToken.objects.get(code=code)
        except EmailVerificationToken.DoesNotExist, e:
            raise EmailVerificationError('invalid_code')

        if code.person != self:
            raise EmailVerificationError('wrong_person')
        elif code.is_used:
            raise EmailVerificationError('code_used')
        elif code.email != self.email:
            raise EmailVerificationError('email_changed')
        elif self.is_email_verified:
            raise EmailVerificationError('already_verified')
        else:
            code.mark_used()

            self.email_verified_at = timezone.now()
            self.save()


class EventMetaBase(models.Model):
    event = models.OneToOneField('core.Event', primary_key=True, related_name='%(class)s')
    admin_group = models.ForeignKey('auth.Group')

    class Meta:
        abstract = True

    def is_user_admin(self, user):
        if not user.is_authenticated():
            return False

        if user.is_superuser:
            return True

        return user.groups.filter(pk=self.admin_group.pk).exists()

    @classmethod
    def get_or_create_group(cls, event, suffix):
        from django.contrib.auth.models import Group
        from django.contrib.contenttypes.models import ContentType

        ctype = ContentType.objects.get_for_model(cls)

        group_name = '{installation_slug}-{event_slug}-{app_label}-{suffix}'.format(
            installation_slug=settings.TURSKA_INSTALLATION_SLUG,
            event_slug=event.slug,
            app_label=ctype.app_label,
            suffix=suffix,
        )
        return Group.objects.get_or_create(name=group_name)


ONE_TIME_CODE_LENGTH = 40
ONE_TIME_CODE_ALPHABET = '0123456789abcdef'


class OneTimeCode(models.Model):
    code = models.CharField(max_length=63, unique=True)
    person = models.ForeignKey(Person)
    created_at = models.DateTimeField(auto_now_add=True)
    used_at = models.DateTimeField(null=True, blank=True)
    state = models.CharField(
        max_length=8,
        choices=[
            ('valid', u'Kelvollinen'),
            ('used', u'Käytetty'),
            ('revoked', u'Mitätöity'),
        ]
    )

    @property
    def is_used(self):
        return self.used_at is not None

    def __unicode__(self):
        return self.code

    def save(self, *args, **kwargs):
        if not self.code:
            from random import choice
            self.code = "".join(choice(ONE_TIME_CODE_ALPHABET) for _ in range(ONE_TIME_CODE_LENGTH))

        return super(OneTimeCode, self).save(*args, **kwargs)

    def revoke(self):
        assert self.state == 'valid'
        self.state = 'revoked'
        self.used_at = timezone.now()
        self.save()

    def render_message_subject(self, request):
        raise NotImplemented()

    def render_message_body(self, request):
        raise NotImplemented()

    def send(self, request):
        from django.core.mail import EmailMessage

        EmailMessage(
            subject=self.render_message_subject(request),
            body=self.render_message_body(request),
            to=(self.person.name_and_email,),
        ).send(fail_silently=True)

    def mark_used(self):
        assert not self.is_used
        self.used_at = timezone.now()
        self.save()

    class Meta:
        abstract = True
        index_together = [
            ('person', 'state'),
        ]


class PasswordResetToken(OneTimeCode):
    ip_address = models.CharField(max_length=45, blank=True) # IPv6

    def render_message_subject(self, request):
        return u'{settings.TURSKA_INSTALLATION_NAME}: Salasanan vaihto'.format(settings=settings)

    def render_message_body(self, request):
        vars = dict(
            link=request.build_absolute_uri(url('core_password_reset_view', self.code))
        )

        return render_to_string('core_password_reset_message.eml', vars, context_instance=RequestContext(request, {}))


class EmailVerificationToken(OneTimeCode):
    email = models.CharField(max_length=255)

    def save(self, *args, **kwargs):
        if self.person and not self.email:
            self.email = self.person.email

        return super(EmailVerificationToken, self).save(*args, **kwargs)

    def render_message_subject(self, request):
        return u'{settings.TURSKA_INSTALLATION_NAME}: Vahvista sähköpostiosoitteesi!'.format(settings=settings)

    def render_message_body(self, request):
        vars = dict(
            link=request.build_absolute_uri(url('core_email_verification_view', self.code))
        )

        return render_to_string('core_email_verification_message.eml', vars, context_instance=RequestContext(request, {}))


__all__ = [
    'BIRTH_DATE_HELP_TEXT',
    'Event',
    'EventMetaBase',
    'EMAIL_LENGTH',
    'Person',
    'PHONE_NUMBER_LENGTH',
    'Venue',
]
