# Generated by Django 2.1.3 on 2018-11-02 12:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('test_m2m', '0004_line_test_year'),
    ]

    operations = [
        migrations.AlterField(
            model_name='line',
            name='test_year',
            field=models.DateField(verbose_name='参试年份'),
        ),
    ]