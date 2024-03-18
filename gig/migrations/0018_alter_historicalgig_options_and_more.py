# Generated by Django 4.2.10 on 2024-03-17 22:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('gig', '0017_auto_20240316_1133'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='historicalgig',
            options={'get_latest_by': ('history_date', 'history_id'), 'ordering': ('-history_date', '-history_id'), 'verbose_name': 'historical gig', 'verbose_name_plural': 'historical gigs'},
        ),
        migrations.AlterField(
            model_name='historicalgig',
            name='history_date',
            field=models.DateTimeField(db_index=True),
        ),
    ]
