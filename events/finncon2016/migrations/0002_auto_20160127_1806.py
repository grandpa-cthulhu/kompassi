# -*- coding: utf-8 -*-
# Generated by Django 1.9.1 on 2016-01-27 16:06
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('finncon2016', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='signupextra',
            name='dead_dog',
            field=models.BooleanField(default=False, help_text='Dead dogit ovat heti tapahtuman j\xe4lkeen j\xe4rjestett\xe4v\xe4t kestit kaikille t\xe4ysik\xe4isille ty\xf6voimaan kuuluville. Dead dogit j\xe4rjestet\xe4\xe4n TKL:n bussireittien tavoitettavissa olevassa paikassa. Ilmoittautuminen ei ole sitova.', verbose_name='Osallistun dead dogeihin'),
        ),
        migrations.AddField(
            model_name='signupextra',
            name='shirt_size',
            field=models.CharField(blank=True, choices=[('NO_SHIRT', 'Ei paitaa'), ('XS', 'XS Unisex'), ('S', 'S Unisex'), ('M', 'M Unisex'), ('L', 'L Unisex'), ('XL', 'XL Unisex'), ('XXL', 'XXL Unisex'), ('3XL', '3XL Unisex'), ('4XL', '4XL Unisex'), ('5XL', '5XL Unisex'), ('LF_XS', 'XS Ladyfit'), ('LF_S', 'S Ladyfit'), ('LF_M', 'M Ladyfit'), ('LF_L', 'L Ladyfit'), ('LF_XL', 'XL Ladyfit')], help_text='Ajoissa ilmoittautuneet v\xe4nk\xe4rit saavat maksuttoman ty\xf6voimapaidan. Kokotaulukot: <a href="http://www.bc-collection.eu/uploads/sizes/TU004.jpg" target="_blank">unisex-paita</a>, <a href="http://www.bc-collection.eu/uploads/sizes/TW040.jpg" target="_blank">ladyfit-paita</a>', max_length=8, null=True, verbose_name='Paidan koko'),
        ),
    ]
