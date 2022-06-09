from django.core.management import BaseCommand
from django_countries import countries
from localflavor.us.us_states import CONTIGUOUS_STATES

from course_discovery.apps.core.models import Country, State


class Command(BaseCommand):
    def handle(self, *args, **options):
        Country.objects.bulk_create(
            [Country(country=code) for code in dict(countries).keys()],
            ignore_conflicts=True
        )
        State.objects.bulk_create(
            [State(state=state[0]) for state in CONTIGUOUS_STATES],
            ignore_conflicts=True
        )
