"""
    This file is part of Gig-o-Matic

    Gig-o-Matic is free software: you can redistribute it and/or modify
    it under the terms of the GNU General Public License as published by
    the Free Software Foundation, either version 3 of the License, or
    (at your option) any later version.

    This program is distributed in the hope that it will be useful,
    but WITHOUT ANY WARRANTY; without even the implied warranty of
    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
    GNU General Public License for more details.

    You should have received a copy of the GNU General Public License
    along with this program.  If not, see <https://www.gnu.org/licenses/>.
"""
from django.core.files.storage import FileSystemStorage
from icalendar import Calendar, Event
from django.utils import timezone, translation
from django.utils.translation import gettext_lazy as _

filesys = FileSystemStorage("calfeeds","calfeeds")

def save_calfeed(tag, content):
    with filesys.open('{0}.txt'.format(tag),mode='w') as f:
        f.write(content)

def get_calfeed(tag):
    with filesys.open('{0}.txt'.format(tag),mode='r') as f:
        s = f.readline()
    return s


def make_calfeed(the_title, the_events, the_language):
    """ construct an ical-compliant stream from a list of events """

    def _make_summary(event):
        """ summary is the title, plus band name and status """
        return '{0}:{1} {2}'.format(event.band.name, event.title, event.status)

    def _make_description(event):
        """ description is the details, plus the setlist """
        x = ''
        if e.details:
            x = '{0}'.format(e.details.replace('\r\n', '\\n'))
        if e.setlist:
            x = '{0}\\n\\n{1}'.format(x, e.setlist.replace('\r\n', '\\n'))
        return x

    # set up language
    cal = Calendar()
    with translation.override(the_language):
        cal.add('prodid', '-//Gig-o-Matic//gig-o-matic.com//')
        cal.add('version', '2.0')
        cal.add('X-WR-CALNAME', the_title)
        cal.add('X-WR-CALDESC', '{0} {1}'.format(_('Gig-o-Matic calendar for'),the_title))
        for e in the_events:
            with timezone.override(e.band.timezone):
                event = Event()
                event.add('summary', _make_summary(e))
                event.add('dtstart', e.date)
                event.add('dtend', e.enddate)
                event.add('description', _make_description(e))
                event.add('location', e.address)
                event.add('url', 'http://www.gig-o-matic.com/gig/{0}'.format(e.id))
                # todo don't hardwire the URL
                # todo go2 also has sequence:0, status:confirmed, and transp:opaque attributes - need those?
                cal.add_component(event)
    return cal.to_ical()
