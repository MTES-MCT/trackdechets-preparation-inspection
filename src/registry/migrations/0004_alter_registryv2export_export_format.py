# Generated by Django 5.2 on 2025-05-08 20:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('registry', '0003_alter_registryv2export_registry_type_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='registryv2export',
            name='export_format',
            field=models.CharField(choices=[('CSV', 'Texte (.csv)'), ('XLSX', 'Excel (.xlsx)')], default='CSV', max_length=20, verbose_name="Format d'export"),
        ),
    ]
