from django.db import migrations


class Migration(migrations.Migration):
    dependencies = [
        ("sheets", "0025_remove_computedinspectiondata_icpe_2760_graph_data_and_more"),
    ]

    operations = [
        migrations.RemoveField(
            model_name="computedinspectiondata",
            name="icpe_2760_data",
        ),
        migrations.RemoveField(
            model_name="computedinspectiondata",
            name="icpe_2770_data",
        ),
        migrations.RemoveField(
            model_name="computedinspectiondata",
            name="icpe_2790_data",
        ),
    ]
