"""
Django command to wait for the database to be availaible.
"""
import time

from psycopg2 import OperationalError as Psycog2Error

from django.db.utils import OperationalError
from django.core.management import BaseCommand


class Command(BaseCommand):
    """Django command to wait for database"""

    def handle(self, *args, **options):
        self.stdout.write('\nWaiting for database...')
        db_up = False
        while db_up is False:
            try:
                self.check(databases=['default'])
                db_up = True
            except (Psycog2Error, OperationalError):
                self.stdout.write('Database unavailable, \
                                  waiting for 1 second...')
                time.sleep(1)

        self.stdout.write('Database available!')
