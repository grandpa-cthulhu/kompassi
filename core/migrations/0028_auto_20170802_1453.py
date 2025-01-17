# Generated by Django 1.10.7 on 2017-08-02 11:53
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ("core", "0027_event_panel_css_class"),
    ]

    operations = [
        migrations.AlterField(
            model_name="event",
            name="organization",
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.CASCADE,
                related_name="events",
                to="core.Organization",
                verbose_name="Järjestäjätaho",
            ),
        ),
    ]
