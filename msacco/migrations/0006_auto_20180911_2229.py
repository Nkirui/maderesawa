# Generated by Django 2.0.7 on 2018-09-11 19:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('msacco', '0005_auto_20180911_2227'),
    ]

    operations = [
        migrations.AlterField(
            model_name='driverprofile',
            name='dl',
            field=models.CharField(default='', max_length=8, unique=True, verbose_name='Driving Licence'),
        ),
    ]
