# Generated by Django 3.2.6 on 2021-09-24 15:05

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Api', '0006_auto_20210924_1559'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='professor',
            name='name',
        ),
        migrations.RemoveField(
            model_name='professor',
            name='surname',
        ),
        migrations.RemoveField(
            model_name='student',
            name='name',
        ),
        migrations.RemoveField(
            model_name='student',
            name='surname',
        ),
    ]
