# Generated by Django 4.2.6 on 2023-11-03 19:56

from django.conf import settings
import django.core.validators
from django.db import migrations, models
import django.db.models.deletion
import uuid


class Migration(migrations.Migration):
    dependencies = [
        ("core", "0038_alter_person_discord_handle"),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ("forms", "0006_formresponse"),
    ]

    operations = [
        migrations.CreateModel(
            name="EventForm",
            fields=[
                ("id", models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name="ID")),
                ("title", models.CharField(max_length=255)),
                ("description", models.TextField(blank=True, default="")),
                ("active", models.BooleanField(default=True)),
                (
                    "standalone",
                    models.BooleanField(
                        default=True,
                        help_text="Stand-alone forms can be used via the generic form views whereas non-stand-alone forms can only be accessed from some other facility.",
                        verbose_name="Stand-alone",
                    ),
                ),
                (
                    "layout",
                    models.CharField(
                        choices=[("horizontal", "Horizontal"), ("vertical", "Vertical")],
                        default="horizontal",
                        max_length=10,
                        verbose_name="Layout",
                    ),
                ),
                (
                    "login_required",
                    models.BooleanField(
                        default=False,
                        help_text="This switch only takes effect in a stand-alone context. In non-stand-alone contexts the use case will direct whether or not login is required.",
                        verbose_name="Login required",
                    ),
                ),
                ("created_at", models.DateTimeField(auto_now_add=True)),
                ("updated_at", models.DateTimeField(auto_now=True)),
                ("fields", models.JSONField()),
                (
                    "slug",
                    models.CharField(
                        help_text='Tekninen nimi eli "slug" näkyy URL-osoitteissa. Sallittuja merkkejä ovat pienet kirjaimet, numerot ja väliviiva. Teknistä nimeä ei voi muuttaa luomisen jälkeen.',
                        max_length=255,
                        validators=[
                            django.core.validators.RegexValidator(
                                message="Tekninen nimi saa sisältää vain pieniä kirjaimia, numeroita sekä väliviivoja.",
                                regex="[a-z0-9-]+",
                            )
                        ],
                        verbose_name="Tekninen nimi",
                    ),
                ),
                (
                    "created_by",
                    models.ForeignKey(
                        blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to=settings.AUTH_USER_MODEL
                    ),
                ),
                (
                    "event",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE, related_name="forms", to="core.event"
                    ),
                ),
            ],
            options={
                "unique_together": {("event", "slug")},
            },
        ),
        migrations.CreateModel(
            name="EventFormResponse",
            fields=[
                ("id", models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ("values", models.JSONField()),
                ("created_at", models.DateTimeField(auto_now_add=True)),
                ("updated_at", models.DateTimeField(auto_now=True)),
                (
                    "created_by",
                    models.ForeignKey(
                        blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to=settings.AUTH_USER_MODEL
                    ),
                ),
                ("form", models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to="forms.eventform")),
            ],
            options={
                "abstract": False,
            },
        ),
        migrations.CreateModel(
            name="GlobalForm",
            fields=[
                ("id", models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name="ID")),
                ("title", models.CharField(max_length=255)),
                ("description", models.TextField(blank=True, default="")),
                ("active", models.BooleanField(default=True)),
                (
                    "standalone",
                    models.BooleanField(
                        default=True,
                        help_text="Stand-alone forms can be used via the generic form views whereas non-stand-alone forms can only be accessed from some other facility.",
                        verbose_name="Stand-alone",
                    ),
                ),
                (
                    "layout",
                    models.CharField(
                        choices=[("horizontal", "Horizontal"), ("vertical", "Vertical")],
                        default="horizontal",
                        max_length=10,
                        verbose_name="Layout",
                    ),
                ),
                (
                    "login_required",
                    models.BooleanField(
                        default=False,
                        help_text="This switch only takes effect in a stand-alone context. In non-stand-alone contexts the use case will direct whether or not login is required.",
                        verbose_name="Login required",
                    ),
                ),
                ("created_at", models.DateTimeField(auto_now_add=True)),
                ("updated_at", models.DateTimeField(auto_now=True)),
                ("fields", models.JSONField()),
                (
                    "slug",
                    models.CharField(
                        help_text='Tekninen nimi eli "slug" näkyy URL-osoitteissa. Sallittuja merkkejä ovat pienet kirjaimet, numerot ja väliviiva. Teknistä nimeä ei voi muuttaa luomisen jälkeen.',
                        max_length=255,
                        unique=True,
                        validators=[
                            django.core.validators.RegexValidator(
                                message="Tekninen nimi saa sisältää vain pieniä kirjaimia, numeroita sekä väliviivoja.",
                                regex="[a-z0-9-]+",
                            )
                        ],
                        verbose_name="Tekninen nimi",
                    ),
                ),
                (
                    "created_by",
                    models.ForeignKey(
                        blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to=settings.AUTH_USER_MODEL
                    ),
                ),
            ],
            options={
                "abstract": False,
            },
        ),
        migrations.CreateModel(
            name="GlobalFormResponse",
            fields=[
                ("id", models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ("values", models.JSONField()),
                ("created_at", models.DateTimeField(auto_now_add=True)),
                ("updated_at", models.DateTimeField(auto_now=True)),
                (
                    "created_by",
                    models.ForeignKey(
                        blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to=settings.AUTH_USER_MODEL
                    ),
                ),
                ("form", models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to="forms.globalform")),
            ],
            options={
                "abstract": False,
            },
        ),
        migrations.RemoveField(
            model_name="formresponse",
            name="created_by",
        ),
        migrations.RemoveField(
            model_name="formresponse",
            name="form",
        ),
        migrations.DeleteModel(
            name="Form",
        ),
        migrations.DeleteModel(
            name="FormResponse",
        ),
    ]
