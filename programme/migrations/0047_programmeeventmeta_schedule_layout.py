# Generated by Django 1.9.5 on 2016-08-13 16:37


from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("programme", "0046_auto_20160811_2319"),
    ]

    operations = [
        migrations.AddField(
            model_name="programmeeventmeta",
            name="schedule_layout",
            field=models.CharField(
                default="reasonable",
                help_text="Some events may opt to make their schedule use the full width of the browser window. This option selects between reasonable width (the default) and full width.",
                max_length=10,
                verbose_name="Schedule layout",
            ),
        ),
    ]
