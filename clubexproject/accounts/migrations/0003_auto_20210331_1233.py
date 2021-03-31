# Generated by Django 3.1.7 on 2021-03-30 23:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0002_auto_20210329_0950'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customer',
            name='subscription',
            field=models.CharField(choices=[('12 Months', '12 Months: $100'), ('1 Month', '1 Month: $10')], default='12 Months', max_length=15),
        ),
        migrations.DeleteModel(
            name='subscription',
        ),
    ]
