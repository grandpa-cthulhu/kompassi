# Generated by Django 1.9.5 on 2016-07-04 20:50


from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ("core", "0023_auto_20160704_2155"),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ("programme", "0038_auto_20160627_2057"),
    ]

    operations = [
        migrations.CreateModel(
            name="ProgrammeFeedback",
            fields=[
                ("id", models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name="ID")),
                (
                    "author_ip_address",
                    models.CharField(
                        blank=True,
                        default="",
                        help_text="The IP address is only visible in the admin interface",
                        max_length=48,
                        verbose_name="IP address",
                    ),
                ),
                (
                    "is_anonymous",
                    models.BooleanField(
                        default=False,
                        help_text="Unless you choose to give feedback anonymously, your name and e-mail address will be shared with the programme host and programme manager. Please note that even if you choose to leave feedback anonymously, abusive feedback can be traced back to you by the administrator of the system.",
                        verbose_name="Give feedback anonymously",
                    ),
                ),
                ("feedback", models.TextField(verbose_name="feedback")),
                ("created_at", models.DateTimeField(auto_now_add=True)),
                ("hidden_at", models.DateTimeField(null=True)),
                ("author", models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to="core.Person")),
                (
                    "hidden_by",
                    models.ForeignKey(
                        blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL
                    ),
                ),
                ("programme", models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to="programme.Programme")),
            ],
            options={
                "verbose_name": "programme feedback",
                "verbose_name_plural": "programme feedback",
            },
        ),
    ]
