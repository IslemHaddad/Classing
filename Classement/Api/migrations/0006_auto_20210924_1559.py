# Generated by Django 3.2.6 on 2021-09-24 14:59

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('Api', '0005_auto_20210924_1439'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='faculty',
            options={'verbose_name_plural': 'Faculties'},
        ),
        migrations.AlterModelOptions(
            name='speciality',
            options={'verbose_name_plural': 'Specialities'},
        ),
        migrations.AlterModelOptions(
            name='university',
            options={'verbose_name_plural': 'Universities'},
        ),
        migrations.AddField(
            model_name='faculty',
            name='university',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='Api.university'),
        ),
        migrations.RemoveField(
            model_name='departement',
            name='faculty',
        ),
        migrations.AddField(
            model_name='departement',
            name='faculty',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='Api.faculty'),
        ),
    ]
