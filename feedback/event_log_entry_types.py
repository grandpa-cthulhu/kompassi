from django.utils.translation import gettext_lazy as _

from event_log import registry


registry.register(
    name="feedback.feedbackmessage.created",
    message=_("Feedback received from {entry.feedback_message.author_display_name}"),
    email_body_template="feedback_message_created.eml",
    email_reply_to=lambda entry: (entry.created_by.email,) if entry.created_by else None,
)
