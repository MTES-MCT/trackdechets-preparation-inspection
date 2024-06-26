# Generated by Django 5.0.4 on 2024-06-07 09:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('sheets', '0045_computedinspectiondata_non_dangerous_waste_stats_data'),
    ]

    operations = [
        migrations.RenameField(
            model_name='computedinspectiondata',
            old_name='icpe_2760_data',
            new_name='icpe_2760_1_data',
        ),
        migrations.RenameField(
            model_name='computedinspectiondata',
            old_name='icpe_2760_graph',
            new_name='icpe_2760_1_graph',
        ),
        migrations.AddField(
            model_name='computedinspectiondata',
            name='icpe_2760_2_data',
            field=models.TextField(blank=True),
        ),
        migrations.AddField(
            model_name='computedinspectiondata',
            name='icpe_2760_2_graph',
            field=models.TextField(blank=True),
        ),
        migrations.AddField(
            model_name='computedinspectiondata',
            name='icpe_2771_data',
            field=models.TextField(blank=True),
        ),
        migrations.AddField(
            model_name='computedinspectiondata',
            name='icpe_2771_graph',
            field=models.TextField(blank=True),
        ),
        migrations.AddField(
            model_name='computedinspectiondata',
            name='icpe_2791_data',
            field=models.TextField(blank=True),
        ),
        migrations.AddField(
            model_name='computedinspectiondata',
            name='icpe_2791_graph',
            field=models.TextField(blank=True),
        ),
    ]
