# Generated by Django 3.0 on 2020-01-11 18:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('gig', '0011_auto_20200111_1335'),
    ]

    operations = [
        migrations.AlterField(
            model_name='plan',
            name='feedback_value',
            field=models.IntegerField(null=True),
        ),
    ]
