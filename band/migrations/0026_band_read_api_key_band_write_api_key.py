# Generated by Django 4.2.17 on 2025-02-27 16:34

import uuid
from django.db import migrations, models, transaction


def add_api_keys(apps, schema_editor):
    Band = apps.get_model('band', 'Band')
    with transaction.atomic():
        update_list = []
        for band in Band.objects.filter(read_api_key__isnull=True):
            band.read_api_key = str(uuid.uuid4())
            band.write_api_key = str(uuid.uuid4())
            update_list.append(band)
        Band.objects.bulk_update(update_list, ['read_api_key', 'write_api_key'])

def remove_api_keys(apps, schema_editor):
    Band = apps.get_model('band', 'Band')
    with transaction.atomic():
        Band.objects.update(read_api_key=None, write_api_key=None)


class Migration(migrations.Migration):

    dependencies = [
        ('band', '0025_alter_band_default_language'),
    ]

    operations = [
        migrations.AddField(
            model_name='band',
            name='read_api_key',
            field=models.CharField(blank=True, max_length=200, null=True),
        ),
        migrations.AddField(
            model_name='band',
            name='write_api_key',
            field=models.CharField(blank=True, max_length=200, null=True),
        ),
        migrations.RunPython(add_api_keys, remove_api_keys),
    ]
