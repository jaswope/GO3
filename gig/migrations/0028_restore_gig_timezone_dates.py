# Generated by Django 4.2.15 on 2025-03-02 00:05

from django.db import migrations
from django.utils import timezone
import pytz


def restore_dates(apps, schema_editor):
    """
    make gigs timezone-aware again. If there was previously an aware date, use it, 
    otherwise use the band's timezone
    """

    def _shift(date, zone):
        d = timezone.make_naive(date)
        return timezone.make_aware(d,zone)

    Gig = apps.get_model('gig', 'Gig')
    for g in Gig.objects.all():

        """ 
        There was no safe date, so this gig must be too new. In that case,
        use the band's timezone to shift whatever the date is to the right timezone
        """
        zone = pytz.timezone(g.band.timezone)
        g.date = _shift(g.date, zone)
        g.setdate = _shift(g.setdate, zone) if g.setdate else None
        g.enddate = _shift(g.enddate, zone) if g.enddate else None

        g.save()

def unrestore_dates(apps, schema_editor):
    """ do nothing, we should not have to undo this! """
    pass

class Migration(migrations.Migration):

    dependencies = [
        ('gig', '0027_alter_gig_date_alter_historicalgig_date'),
    ]


    operations = [
        migrations.RunPython(restore_dates, unrestore_dates)
    ]
