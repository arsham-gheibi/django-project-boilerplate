"""
Django Command to wait for database to be available
"""
import time

from psycopg import OperationalError as PsycopgError

from django.db.utils import OperationalError
from django.core.management.base import BaseCommand


class Command(BaseCommand):
    """ Django Command to wait for database """

    def handle(self, *args, **options):
        """ Entrypoint for command """
        self.stdout.write('Waiting for database...')
        db_up = False
        while db_up is False:
            try:
                self.check(databases=['default'])
                db_up = True
            except (PsycopgError, OperationalError):
                self.stdout.write('Database Unavailable, wating 1 second...')
                time.sleep(1)

        self.stdout.write(self.style.SUCCESS('Database available!'))
