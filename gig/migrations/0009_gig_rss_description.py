# Generated by Django 3.0 on 2020-01-06 23:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('gig', '0008_auto_20200105_1821'),
    ]

    operations = [
        migrations.AddField(
            model_name='gig',
            name='rss_description',
            field=models.TextField(blank=True, null=True),
        ),
    ]
