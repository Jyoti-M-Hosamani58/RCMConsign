# Generated by Django 3.0 on 2025-01-28 20:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('consign_app', '0060_addconsignment_branchcode'),
    ]

    operations = [
        migrations.AddField(
            model_name='addconsignment',
            name='tbbAt',
            field=models.CharField(max_length=150, null=True),
        ),
        migrations.AddField(
            model_name='addconsignmenttemp',
            name='branchcode',
            field=models.CharField(max_length=150, null=True),
        ),
        migrations.AddField(
            model_name='addconsignmenttemp',
            name='tbbAt',
            field=models.CharField(max_length=150, null=True),
        ),
    ]
