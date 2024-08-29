from django.conf import settings


def settings_processor(request):
    # return the value you want as a dictionnary. you may add multiple values in there.
    return {"DISPLAY_ROADCONTROL_MENU": settings.DISPLAY_ROADCONTROL_MENU}
