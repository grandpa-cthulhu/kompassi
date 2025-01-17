# Generated by Django 1.10.8 on 2018-02-03 21:57
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("matsucon2018", "0002_auto_20180203_2326"),
    ]

    operations = [
        migrations.AddField(
            model_name="signupextra",
            name="shirt_size",
            field=models.CharField(
                choices=[
                    ("NO_SHIRT", "En halua paitaa"),
                    ("S", "S"),
                    ("M", "M"),
                    ("L", "L"),
                    ("XL", "XL"),
                    ("OTHER", "Muu koko (kerro Vapaa sana -kentässä)"),
                ],
                default="NO_SHIRT",
                max_length=8,
                verbose_name="Työvoiman T-paidan koko",
            ),
        ),
    ]
