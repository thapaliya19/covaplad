# Generated by Django 3.1.2 on 2020-10-17 17:05

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ("donor", "0002_auto_20201017_2045"),
    ]

    operations = [
        migrations.AlterField(
            model_name="disease",
            name="icd_code",
            field=models.CharField(max_length=10, unique=True, verbose_name="ICD Code"),
        ),
        migrations.AlterField(
            model_name="donor",
            name="blood_group",
            field=models.CharField(max_length=3, verbose_name="Blood Group"),
        ),
        migrations.AlterField(
            model_name="donor",
            name="height",
            field=models.DecimalField(
                decimal_places=2, max_digits=3, verbose_name="height (in feet)"
            ),
        ),
        migrations.AlterField(
            model_name="donor",
            name="id",
            field=models.OneToOneField(
                db_column="id",
                on_delete=django.db.models.deletion.CASCADE,
                primary_key=True,
                serialize=False,
                to=settings.AUTH_USER_MODEL,
                verbose_name="ID",
            ),
        ),
        migrations.AlterField(
            model_name="donor",
            name="last_symptom_date",
            field=models.DateField(verbose_name="COVID Last Symptom Date"),
        ),
        migrations.AlterField(
            model_name="donor",
            name="test_report",
            field=models.TextField(blank=True, verbose_name="Test Report"),
        ),
        migrations.AlterField(
            model_name="donor",
            name="weight",
            field=models.DecimalField(
                decimal_places=2, max_digits=3, verbose_name="weight (in kg)"
            ),
        ),
    ]
