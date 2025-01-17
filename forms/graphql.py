from django.conf import settings

import graphene
from graphene_django import DjangoObjectType
from graphene.types.generic import GenericScalar

from core.utils import get_ip

from .models import EventSurvey, EventForm, GlobalForm, EventFormResponse, GlobalFormResponse


DEFAULT_LANGUAGE: str = settings.LANGUAGE_CODE


class EventFormType(DjangoObjectType):
    fields = graphene.Field(
        GenericScalar,
        enrich=graphene.Boolean(
            description=(
                "Enriched fields have dynamic choices populated for them. This is the default. "
                'Pass enrich: false to get access to "raw" unenriched fields. This is used by the form editor.'
            ),
        ),
    )

    @staticmethod
    def resolve_fields(parent: EventForm, info, enrich: bool = True):
        if enrich:
            return parent.enriched_fields
        else:
            return parent.fields

    class Meta:
        model = EventForm
        fields = ("slug", "title", "description", "thank_you_message", "layout")


class EventSurveyType(DjangoObjectType):
    is_active = graphene.Field(graphene.NonNull(graphene.Boolean))

    @staticmethod
    def resolve_is_active(parent: EventSurvey, info) -> bool:
        return parent.is_active

    form = graphene.Field(EventFormType, lang=graphene.String())

    @staticmethod
    def resolve_form(
        parent: EventSurvey,
        info,
        lang: str = DEFAULT_LANGUAGE,
    ) -> EventForm | None:
        return parent.get_form(lang)

    class Meta:
        model = EventSurvey
        fields = (
            "slug",
            "active_from",
            "active_until",
        )


class EventSurveyResponseType(DjangoObjectType):
    class Meta:
        model = EventFormResponse
        fields = ("id", "form_data", "created_at")


class CreateEventSurveyResponse(graphene.Mutation):
    class Arguments:
        event_slug = graphene.String(required=True)
        survey_slug = graphene.String(required=True)
        form_data = GenericScalar(required=True)
        locale = graphene.String()

    response = graphene.Field(EventSurveyResponseType)

    @staticmethod
    def mutate(
        root,
        info,
        event_slug: str,
        survey_slug: str,
        form_data: str,
        locale: str = "",
    ):
        survey = EventSurvey.objects.get(event__slug=event_slug, slug=survey_slug)
        form = survey.get_form(locale)

        ip_address = get_ip(info.context)
        created_by = user if (user := info.context.user) and user.is_authenticated else None

        response = EventFormResponse.objects.create(
            form=form,
            form_data=form_data,
            created_by=created_by,
            ip_address=ip_address,
        )

        return CreateEventSurveyResponse(response=response)  # type: ignore
