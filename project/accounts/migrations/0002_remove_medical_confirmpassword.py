# Generated by Django 4.1.2 on 2022-11-03 20:18

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='medical',
            name='confirmPassword',
        ),
    ]