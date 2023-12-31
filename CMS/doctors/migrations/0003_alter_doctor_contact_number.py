# Generated by Django 4.2.2 on 2023-07-27 05:58

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('doctors', '0002_doctor_entered_by'),
    ]

    operations = [
        migrations.AlterField(
            model_name='doctor',
            name='contact_number',
            field=models.CharField(max_length=10, validators=[django.core.validators.RegexValidator(code='invalid_phone_number', message='Phone number must be entered in the format: "9999999999". Exactly 10 digits allowed.', regex='^\\+?[0-9]{10}$')]),
        ),
    ]
