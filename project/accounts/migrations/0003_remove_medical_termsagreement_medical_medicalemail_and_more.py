# Generated by Django 4.1.2 on 2022-11-04 10:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0002_remove_medical_confirmpassword'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='medical',
            name='termsAgreement',
        ),
        migrations.AddField(
            model_name='medical',
            name='medicalEmail',
            field=models.EmailField(default=0, max_length=254),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='medical',
            name='medicalPhoneNo',
            field=models.BigIntegerField(default=0),
            preserve_default=False,
        ),
    ]
