# Generated by Django 2.2.17 on 2021-02-23 21:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("programme", "0103_programme_ropecon2021_blocked_time_slots"),
    ]

    operations = [
        migrations.AddField(
            model_name="programme",
            name="ropecon2021_larp_physical_or_virtual",
            field=models.CharField(
                choices=[
                    ("physical_only", "Physical con"),
                    ("virtual_only", "Virtual con"),
                    ("physical_or_virtual", "Both"),
                ],
                default="physical_only",
                help_text="Select the event form appropriate for the larp you have planned.",
                max_length=19,
                null=True,
                verbose_name="I am submitting a larp for",
            ),
        ),
        migrations.AlterField(
            model_name="programme",
            name="ropecon2021_blocked_time_slots",
            field=models.ManyToManyField(
                blank=True,
                help_text="Select the times when you are <b>NOT able</b> to run your larp. In other words, leave the times that you would be able to run your larp unselected!<br/>If you have a more specific request in mind regarding your schedule (for example, you would like to run your larp late at night), please let us know in the Comments section below.<br/>In this section, we would like to know more about how work or volunteer shifts, public transport schedules and other factors might be impacting your schedule. For example, if you need to leave the venue by 11pm to be able to catch the last bus to your accommodation.",
                related_name="_programme_ropecon2021_blocked_time_slots_+",
                to="ropecon2021.TimeSlot",
                verbose_name="When are you NOT able to run your larp?",
            ),
        ),
        migrations.AlterField(
            model_name="programme",
            name="ropecon2021_rpg_clarifications",
            field=models.TextField(
                blank=True,
                default="",
                help_text="Specify here if you have any clarifications or if you have anything to expand upon regarding the above questions.",
                null=True,
                verbose_name="Any clarifications?",
            ),
        ),
    ]
