# Generated by Django 4.2.11 on 2024-04-03 02:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('member', '0017_alter_member_display_name_alter_member_images_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='memberpreferences',
            name='agenda_show_time',
            field=models.BooleanField(default=True, verbose_name='Show gig time on schedule'),
        ),
        migrations.AlterField(
            model_name='memberpreferences',
            name='calendar_show_only_committed',
            field=models.BooleanField(default=False, verbose_name='Calendar shows only gigs I can do (or maybe can do)'),
        ),
        migrations.AlterField(
            model_name='memberpreferences',
            name='calendar_show_only_confirmed',
            field=models.BooleanField(default=False, verbose_name='Calendar shows only confirmed gigs'),
        ),
        migrations.AlterField(
            model_name='memberpreferences',
            name='hide_canceled_gigs',
            field=models.BooleanField(default=False, verbose_name='Hide canceled gigs'),
        ),
        migrations.AlterField(
            model_name='memberpreferences',
            name='language',
            field=models.CharField(choices=[('de', 'German'), ('en-US', 'English (US)'), ('en-GB', 'English (UK, AU, NZ, ...)'), ('fr', 'French'), ('it', 'Italian')], default='en-US', max_length=200, verbose_name='Language'),
        ),
        migrations.AlterField(
            model_name='memberpreferences',
            name='share_email',
            field=models.BooleanField(default=False, verbose_name='Share my email'),
        ),
        migrations.AlterField(
            model_name='memberpreferences',
            name='share_profile',
            field=models.BooleanField(default=True, verbose_name='Share my profile'),
        ),
    ]
