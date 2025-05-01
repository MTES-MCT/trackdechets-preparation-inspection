import random

import factory
from django.contrib.gis.geos import Point
from django.utils import timezone

from common.sirets import generate_siret

from .models import CartoCompany

MIN_LONGITUDE = -5.142222  # Westernmost point
MAX_LONGITUDE = 8.230278  # Easternmost point
MIN_LATITUDE = 42.332778  # Southernmost point
MAX_LATITUDE = 51.089167


def rand_lon():
    return random.uniform(MIN_LONGITUDE, MAX_LONGITUDE)


def rand_lat():
    return random.uniform(MIN_LATITUDE, MAX_LATITUDE)


def rand_coord():
    return Point(x=rand_lon(), y=-rand_lat())


class CartoCompanyFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = CartoCompany

    siret = factory.LazyFunction(generate_siret)
    nom_etablissement = factory.Sequence(lambda n: f"Company {n}")

    coords = factory.LazyFunction(rand_coord)
    date_inscription = timezone.now()
