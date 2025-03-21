# Generated by Django 5.1.6 on 2025-02-27 20:55

from django.db import migrations


def fill_new_reference(apps, schema_editor):
    User = apps.get_model('accounts', 'User')
    for user in User.objects.all():
        if user.monaiot_connexion or  user.monaiot_signup:
            if user.monaiot_connexion:
                user.oidc_connexion = "MONAIOT"
            if user.monaiot_signup:
                user.oidc_signup = "MONAIOT"
            user.save()

class Migration(migrations.Migration):
    dependencies = [
        ('accounts', '0008_user_oidc_connexion_user_oidc_signup'),
    ]

    operations = [migrations.RunPython(fill_new_reference)]
