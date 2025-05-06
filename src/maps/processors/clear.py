import datetime as dt

from ..models import DepartementsComputation, FranceComputation, InstallationsComputation, RegionsComputation


def clear_figs():
    # clear data older than year - 1
    FranceComputation.objects.filter(year__lt=dt.date.today().year - 1).delete()
    InstallationsComputation.objects.filter(year__lt=dt.date.today().year - 1).delete()
    RegionsComputation.objects.filter(year__lt=dt.date.today().year - 1).delete()
    DepartementsComputation.objects.filter(year__lt=dt.date.today().year - 1).delete()
