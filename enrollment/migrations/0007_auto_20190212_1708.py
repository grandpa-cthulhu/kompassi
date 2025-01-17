# Generated by Django 2.1.5 on 2019-02-12 15:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("enrollment", "0006_auto_20190120_1555"),
    ]

    operations = [
        migrations.AddField(
            model_name="enrollment",
            name="traconjv_avow_and_affirm",
            field=models.BooleanField(
                default=False,
                verbose_name="Vakuutan olevani lain tarkoittamalla tavalla rehellinen ja luotettava ja henkilökohtaisilta ominaisuuksiltani tehtävään sopiva, eikä minulla ole voimassaolevia tai vanhoja tuomioita tai rikosrekisteriä.",
            ),
        ),
        migrations.AlterField(
            model_name="enrollment",
            name="traconjv_expiring",
            field=models.DateField(
                blank=True,
                help_text="Päivämäärä muodossa 24.2.1994 tai 1994-02-24",
                null=True,
                verbose_name="Milloin nykyinen JV-korttisi on umpeutumassa?",
            ),
        ),
        migrations.AlterField(
            model_name="enrollment",
            name="traconjv_solemnly_swear",
            field=models.BooleanField(
                default=False,
                verbose_name="Vakuutan antamani tiedot oikeiksi. Sitoudun maksamaan kurssin hinnan täysimääräisenä, mikäli en pysty osallistumaan peruskurssille 30.–31.3., 6.–7.4. ja 13.4 tai järjestyksenvalvojana Tracon 2019- ja Tracon 2020-tapahtumiin.",
            ),
        ),
    ]
