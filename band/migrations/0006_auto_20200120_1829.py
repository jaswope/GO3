# Generated by Django 3.0 on 2020-01-20 23:29

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('band', '0005_auto_20200119_2147'),
    ]

    operations = [
        migrations.AlterField(
            model_name='assoc',
            name='default_section',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='default_assocs', to='band.Section'),
        ),
    ]
