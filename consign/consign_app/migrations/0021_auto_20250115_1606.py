# Generated by Django 3.0 on 2025-01-15 10:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('consign_app', '0020_auto_20250115_1543'),
    ]

    operations = [
        migrations.AlterField(
            model_name='rate',
            name='cod',
            field=models.FloatField(null=True),
        ),
    ]
