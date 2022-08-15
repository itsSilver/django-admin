# Generated by Django 4.0.4 on 2022-05-27 21:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mainapp', '0005_alter_occorrenze_segnalazione'),
    ]

    operations = [
        migrations.AddField(
            model_name='occorrenze',
            name='rif_ticket',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
        migrations.AddField(
            model_name='segnalazioni',
            name='rif_ticket',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
        migrations.AddField(
            model_name='soluzioni',
            name='rif_ticket',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
    ]