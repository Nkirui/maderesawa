# Generated by Django 2.0.7 on 2018-09-11 21:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('msacco', '0007_auto_20180911_2358'),
    ]

    operations = [
        migrations.AlterField(
            model_name='driverprofile',
            name='emp_rmks',
            field=models.CharField(choices=[('Avarage driver', 'Careless driver'), ('Good driver', 'Good driver'), ('Very Good', 'Very Good'), ('Worst driver', 'Worst driver')], default='Good driver', max_length=100, verbose_name='Employer Remarks'),
        ),
    ]
