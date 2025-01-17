# Generated by Django 4.1.7 on 2023-04-15 15:28

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):
    dependencies = [
        ("programme", "0118_alter_programme_photography_and_more"),
        ("mailings", "0009_recipientgroup_programme_category_and_more"),
    ]

    operations = [
        migrations.AddField(
            model_name="recipientgroup",
            name="programme_form",
            field=models.ForeignKey(
                blank=True,
                null=True,
                on_delete=django.db.models.deletion.CASCADE,
                to="programme.alternativeprogrammeform",
            ),
        ),
    ]
