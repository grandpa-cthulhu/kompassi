# Generated by Django 1.10.7 on 2017-08-30 19:37
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ("badges", "0020_auto_20160706_2207"),
    ]

    operations = [
        migrations.AddField(
            model_name="badgeseventmeta",
            name="is_using_fuzzy_reissuance_hack",
            field=models.BooleanField(
                default=False,
                help_text='In Tracon 2017, Japsu forgot to re-issue badges when he flipped the "Real name must be visible" setting. This caused lots of printed badges to be revoked and re-issued. When the fuzzy reissuance hack is active, badges will not get re-issued if the only change is which fields are visible. Combine this with python manage.py rescue_wrongly_revoked_badges.',
                verbose_name="Use fuzzy reissuance hack",
            ),
        ),
        migrations.AlterField(
            model_name="badge",
            name="batch",
            field=models.ForeignKey(
                blank=True,
                null=True,
                on_delete=django.db.models.deletion.SET_NULL,
                related_name="badges",
                to="badges.Batch",
                verbose_name="Printing batch",
            ),
        ),
        migrations.AlterField(
            model_name="badge",
            name="person",
            field=models.ForeignKey(
                blank=True,
                null=True,
                on_delete=django.db.models.deletion.CASCADE,
                related_name="badges",
                to="core.Person",
                verbose_name="Person",
            ),
        ),
        migrations.AlterField(
            model_name="badge",
            name="personnel_class",
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.CASCADE,
                related_name="badges",
                to="labour.PersonnelClass",
                verbose_name="Personnel class",
            ),
        ),
    ]
