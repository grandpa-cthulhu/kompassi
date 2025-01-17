# Generated by Django 2.1.5 on 2019-02-28 20:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("programme", "0083_programme_is_inaccessible"),
    ]

    operations = [
        migrations.AddField(
            model_name="programme",
            name="field_of_expertise",
            field=models.CharField(blank=True, default="", max_length=1023, verbose_name="My field of expertise"),
        ),
        migrations.AddField(
            model_name="programme",
            name="is_available_for_panel",
            field=models.BooleanField(
                default=False,
                help_text="I can participate in a panel discussion on my field of expertise during the convention.",
                verbose_name="Panel discussions",
            ),
        ),
    ]
