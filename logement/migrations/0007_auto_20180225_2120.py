# Generated by Django 2.0 on 2018-02-25 20:20

import django.contrib.gis.db.models.fields
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('logement', '0006_auto_20180225_1722'),
    ]

    operations = [
        migrations.AddField(
            model_name='result',
            name='cr1_result_raster',
            field=django.contrib.gis.db.models.fields.RasterField(blank=True, null=True, srid=4326),
        ),
        migrations.AddField(
            model_name='result',
            name='cr2_result_raster',
            field=django.contrib.gis.db.models.fields.RasterField(blank=True, null=True, srid=4326),
        ),
        migrations.AddField(
            model_name='result',
            name='cr3_result_raster',
            field=django.contrib.gis.db.models.fields.RasterField(blank=True, null=True, srid=4326),
        ),
    ]