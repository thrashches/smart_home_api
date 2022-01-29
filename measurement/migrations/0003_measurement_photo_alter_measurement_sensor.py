# Generated by Django 4.0.1 on 2022-01-29 13:02

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('measurement', '0002_alter_measurement_temperature'),
    ]

    operations = [
        migrations.AddField(
            model_name='measurement',
            name='photo',
            field=models.ImageField(blank=True, null=True, upload_to='', verbose_name='фото'),
        ),
        migrations.AlterField(
            model_name='measurement',
            name='sensor',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='measurements', to='measurement.sensor', verbose_name='датчик'),
        ),
    ]
