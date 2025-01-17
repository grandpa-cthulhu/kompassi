# Generated by Django 4.1.7 on 2023-04-15 07:36

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):
    dependencies = [
        ("programme", "0117_programme_tracon2023_accessibility_warnings_and_more"),
        ("mailings", "0008_auto_20161026_2343"),
    ]

    operations = [
        migrations.AddField(
            model_name="recipientgroup",
            name="programme_category",
            field=models.ForeignKey(
                blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to="programme.category"
            ),
        ),
        migrations.AlterField(
            model_name="recipientgroup",
            name="app_label",
            field=models.CharField(
                choices=[("labour", "Työvoima"), ("programme", "Ohjelma")], max_length=63, verbose_name="Sovellus"
            ),
        ),
    ]
