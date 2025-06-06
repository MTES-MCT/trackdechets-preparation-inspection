# Generated by Django 5.2 on 2025-05-12 09:58

import django.contrib.postgres.indexes
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('maps', '0005_departementscomputation_francecomputation_and_more'),
    ]

    operations = [
        migrations.RemoveIndex(
            model_name='cartocompany',
            name='maps_cartoc_process_d1e834_gin',
        ),
        migrations.RemoveIndex(
            model_name='cartocompany',
            name='maps_cartoc_process_6d0266_gin',
        ),
        migrations.RenameField(
            model_name='cartocompany',
            old_name='processing_operation_dnd',
            new_name='processing_operations_dnd',
        ),
        migrations.RenameField(
            model_name='cartocompany',
            old_name='processing_operation_texs',
            new_name='processing_operations_texs',
        ),
        migrations.AddIndex(
            model_name='cartocompany',
            index=django.contrib.postgres.indexes.GinIndex(fields=['processing_operations_dnd'], name='maps_cartoc_process_53cb78_gin'),
        ),
        migrations.AddIndex(
            model_name='cartocompany',
            index=django.contrib.postgres.indexes.GinIndex(fields=['processing_operations_texs'], name='maps_cartoc_process_a29cf9_gin'),
        ),
    ]
