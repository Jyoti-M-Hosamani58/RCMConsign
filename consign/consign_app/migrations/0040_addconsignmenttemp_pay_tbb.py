# Generated by Django 3.0 on 2025-01-16 19:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('consign_app', '0039_auto_20250117_0042'),
    ]

    operations = [
        migrations.AddField(
            model_name='addconsignmenttemp',
            name='pay_tbb',
            field=models.CharField(max_length=30, null=True),
        ),
    ]
