# Generated by Django 2.0.7 on 2018-09-11 20:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('msacco', '0006_auto_20180911_2229'),
    ]

    operations = [
        migrations.AlterField(
            model_name='driverprofile',
            name='driver_status',
            field=models.CharField(choices=[('Employed', 'Employed'), ('Dismissed', 'Dismissed'), ('Resigned', 'Resigned'), ('Left', 'Left')], default='Employed', max_length=100),
        ),
    ]
