from django.core.management.base import BaseCommand


from django.conf import settings
from sqlalchemy import create_engine
from sqlalchemy.sql import text


wh_engine = create_engine(settings.WAREHOUSE_TEST_URL, pool_pre_ping=True)

class Command(BaseCommand):


    def handle(self, verbosity=0, **options):
        with open('clear.sql', "r") as f:

            query = text(f.read())

        result = wh_engine.engine.execute(query)
        print(result)