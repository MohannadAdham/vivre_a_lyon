# Generated by Django 2.0 on 2018-02-25 15:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('logement', '0003_commune_mpoly'),
    ]

    operations = [
        migrations.AlterField(
            model_name='criterion',
            name='description',
            field=models.TextField(null=True),
        ),
        migrations.AlterField(
            model_name='usercriterion',
            name='weight',
            field=models.DecimalField(decimal_places=3, max_digits=4, null=True),
        ),
    ]