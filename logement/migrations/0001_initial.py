# Generated by Django 2.0 on 2018-02-25 11:17

import django.contrib.gis.db.models.fields
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Commune',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('id_geofla', models.CharField(max_length=24)),
                ('code_com', models.CharField(max_length=3)),
                ('insee_com', models.CharField(max_length=5)),
                ('nom_com', models.CharField(max_length=50)),
                ('superficie', models.BigIntegerField()),
                ('code_dept', models.CharField(max_length=2)),
                ('nom_dept', models.CharField(max_length=30)),
            ],
        ),
        migrations.CreateModel(
            name='Criterion',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=150)),
                ('description', models.TextField()),
                ('raster10', django.contrib.gis.db.models.fields.RasterField(srid=4326)),
                ('raster50', django.contrib.gis.db.models.fields.RasterField(srid=4326)),
            ],
        ),
        migrations.CreateModel(
            name='ResultCommune',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('criterion1_value', models.DecimalField(decimal_places=3, max_digits=6)),
                ('criterion2_value', models.DecimalField(decimal_places=3, max_digits=6)),
                ('criterion3_value', models.DecimalField(decimal_places=3, max_digits=6)),
                ('result_value', models.DecimalField(decimal_places=3, max_digits=6)),
                ('id_commune', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='logement.Commune')),
            ],
        ),
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
            ],
        ),
        migrations.CreateModel(
            name='UserCriterion',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('weight', models.DecimalField(decimal_places=3, max_digits=4)),
                ('id_criterion', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='logement.Criterion')),
            ],
        ),
        migrations.CreateModel(
            name='Result',
            fields=[
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, primary_key=True, serialize=False, to='logement.User')),
                ('result_raster', django.contrib.gis.db.models.fields.RasterField(srid=4326)),
                ('date_time', models.DateTimeField(auto_now=True)),
            ],
        ),
        migrations.AddField(
            model_name='usercriterion',
            name='id_user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='logement.User'),
        ),
        migrations.AddField(
            model_name='user',
            name='criteria',
            field=models.ManyToManyField(through='logement.UserCriterion', to='logement.Criterion'),
        ),
        migrations.AddField(
            model_name='resultcommune',
            name='id_result',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='logement.Result'),
        ),
        migrations.AddField(
            model_name='result',
            name='commune',
            field=models.ManyToManyField(through='logement.ResultCommune', to='logement.Commune'),
        ),
    ]
