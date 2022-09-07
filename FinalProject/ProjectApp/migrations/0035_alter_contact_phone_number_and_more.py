# Generated by Django 4.1 on 2022-09-04 05:47

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("ProjectApp", "0034_alter_userprofile_phone_number"),
    ]

    operations = [
        migrations.AlterField(
            model_name="contact",
            name="phone_number",
            field=models.PositiveIntegerField(
                blank=True,
                null=True,
                validators=[django.core.validators.MaxValueValidator(9999999999)],
            ),
        ),
        migrations.AlterField(
            model_name="userprofile",
            name="phone_number",
            field=models.PositiveIntegerField(
                blank=True,
                null=True,
                validators=[django.core.validators.MaxValueValidator(9999999999)],
            ),
        ),
    ]