# Generated by Django 4.2 on 2023-04-20 08:47

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("sheets", "0013_computedinspectiondata_all_bsd_data_empty"),
    ]

    operations = [
        migrations.AddField(
            model_name="computedinspectiondata",
            name="bsd_canceled_data",
            field=models.JSONField(default=dict),
        ),
    ]