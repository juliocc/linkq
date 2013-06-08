import pprint
from datetime import datetime
import json
import requests
from optparse import make_option

from django.core.management.base import BaseCommand, CommandError
from django.conf import settings
import pytz

from ...models import Link

class Command(BaseCommand):
    args = '<consumer_key access_token>'
    help = 'Import links from an existing pocket account'

    STATUS_UNREAD = 0
    STATUS_READ = 1
    STATUS_DELETED = 2

    def handle(self, *args, **options):
        params = {'consumer_key': args[0],
                  'access_token': args[1],
                  'sort': 'oldest',
                  'state': 'all'}

        r = requests.post('https://getpocket.com/v3/get', data=params)
        data = r.json()
        for id, item in data['list'].iteritems():
            tzinfo = pytz.timezone(settings.TIME_ZONE)

            added = datetime.utcfromtimestamp(int(item['time_added']))
            added = added.replace(tzinfo=tzinfo)

            read = datetime.utcfromtimestamp(int(item['time_read']))
            read = read.replace(tzinfo=tzinfo)

            status = int(item['status'])
            # pprint.pprint(item)
            link = Link.objects.filter(url=item['resolved_url'])
            if link.count() == 0:
                if status == self.STATUS_READ:
                    link = Link.objects.create(url=item['resolved_url'],
                                               title=item['resolved_title'],
                                               created=added,
                                               read=read)
                    self.stdout.write('Created: ' + str(link))
                elif status == self.STATUS_UNREAD:
                    link = Link.objects.create(url=item['resolved_url'],
                                               title=item['resolved_title'],
                                               created=added)
                    self.stdout.write('Created: ' + str(link))
                else:
                    self.stdout.write('Skiped (deleted): ' + item['resolved_url'])


