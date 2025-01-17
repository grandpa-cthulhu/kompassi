# Generated by Django 1.10.8 on 2018-10-19 17:09
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ("labour", "0033_auto_20170802_1500"),
        ("event_log", "0007_entry_ip_address"),
    ]

    operations = [
        migrations.AddField(
            model_name="subscription",
            name="job_category_filter",
            field=models.ForeignKey(
                blank=True,
                help_text="When specified, only entries related to this JobCategory will match the subscription.",
                null=True,
                on_delete=django.db.models.deletion.CASCADE,
                to="labour.JobCategory",
                verbose_name="Job category filter",
            ),
        ),
    ]
