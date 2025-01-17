# Generated by Django 1.10.7 on 2017-09-15 15:45
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ("core", "0029_auto_20170827_1818"),
        ("event_log", "0005_entry_person"),
    ]

    operations = [
        migrations.AddField(
            model_name="entry",
            name="organization",
            field=models.ForeignKey(
                blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to="core.Organization"
            ),
        ),
        migrations.AddField(
            model_name="entry",
            name="search_term",
            field=models.CharField(blank=True, default="", max_length=255),
        ),
    ]
