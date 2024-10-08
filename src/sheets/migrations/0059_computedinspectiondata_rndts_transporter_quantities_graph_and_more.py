# Generated by Django 5.0.7 on 2024-08-13 14:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('sheets', '0058_computedinspectiondata_ssd_table_data'),
    ]

    operations = [
        migrations.AddField(
            model_name='computedinspectiondata',
            name='rndts_transporter_quantities_graph',
            field=models.TextField(blank=True),
        ),
        migrations.AddField(
            model_name='computedinspectiondata',
            name='rndts_transporter_quantities_graph_data',
            field=models.JSONField(default=dict),
        ),
        migrations.AddField(
            model_name='computedinspectiondata',
            name='rndts_transporter_statement_stats_graph',
            field=models.TextField(blank=True),
        ),
        migrations.AddField(
            model_name='computedinspectiondata',
            name='rndts_transporter_statement_stats_graph_data',
            field=models.JSONField(default=dict),
        ),
    ]
