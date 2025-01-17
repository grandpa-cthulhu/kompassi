# Generated by Django 1.9.9 on 2017-02-20 22:18


from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ("feedback", "0001_initial"),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name="Entry",
            fields=[
                ("id", models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name="ID")),
                ("created_at", models.DateTimeField(auto_now_add=True, db_index=True)),
                ("entry_type", models.CharField(max_length=255)),
                (
                    "created_by",
                    models.ForeignKey(
                        blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to=settings.AUTH_USER_MODEL
                    ),
                ),
                (
                    "feedback_message",
                    models.ForeignKey(
                        blank=True,
                        null=True,
                        on_delete=django.db.models.deletion.SET_NULL,
                        to="feedback.FeedbackMessage",
                    ),
                ),
            ],
            options={
                "ordering": ("-created_at",),
                "verbose_name": "log entry",
                "verbose_name_plural": "log entries",
            },
        ),
        migrations.CreateModel(
            name="Subscription",
            fields=[
                ("id", models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name="ID")),
                ("entry_type", models.CharField(max_length=255)),
                ("channel", models.CharField(choices=[("email", "E-mail")], default="email", max_length=5)),
                ("active", models.BooleanField(default=True)),
                ("user", models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                "verbose_name": "subscription",
                "verbose_name_plural": "subscriptions",
            },
        ),
        migrations.AlterIndexTogether(
            name="subscription",
            index_together={("entry_type", "active")},
        ),
    ]
