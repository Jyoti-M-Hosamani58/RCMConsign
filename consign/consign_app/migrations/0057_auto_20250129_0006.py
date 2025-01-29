# Generated by Django 3.0 on 2025-01-28 18:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('consign_app', '0056_auto_20250128_1154'),
    ]

    operations = [
        migrations.RenameField(
            model_name='lcmtemp',
            old_name='area',
            new_name='receiver_GST',
        ),
        migrations.RenameField(
            model_name='lcmtemp',
            old_name='driver_name',
            new_name='receiver_address',
        ),
        migrations.RenameField(
            model_name='lcmtemp',
            old_name='labour',
            new_name='receiver_mobile',
        ),
        migrations.RemoveField(
            model_name='lcmtemp',
            name='date',
        ),
        migrations.RemoveField(
            model_name='lcmtemp',
            name='lcm_no',
        ),
        migrations.RemoveField(
            model_name='lcmtemp',
            name='location',
        ),
        migrations.RemoveField(
            model_name='lcmtemp',
            name='time',
        ),
        migrations.RemoveField(
            model_name='lcmtemp',
            name='vehicle_no',
        ),
        migrations.AddField(
            model_name='branch',
            name='branchcode',
            field=models.CharField(max_length=50, null=True),
        ),
        migrations.AddField(
            model_name='lcm',
            name='branch',
            field=models.CharField(max_length=255, null=True),
        ),
        migrations.AddField(
            model_name='lcm',
            name='branchemail',
            field=models.CharField(max_length=255, null=True),
        ),
        migrations.AddField(
            model_name='lcm',
            name='name',
            field=models.CharField(max_length=255, null=True),
        ),
        migrations.AddField(
            model_name='lcm',
            name='receiver_GST',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='lcm',
            name='receiver_address',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='lcm',
            name='receiver_mobile',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='lcm',
            name='sender_GST',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='lcm',
            name='sender_address',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='lcm',
            name='sender_mobile',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='lcmtemp',
            name='branch',
            field=models.CharField(max_length=255, null=True),
        ),
        migrations.AddField(
            model_name='lcmtemp',
            name='branchemail',
            field=models.CharField(max_length=255, null=True),
        ),
        migrations.AddField(
            model_name='lcmtemp',
            name='collectionLocation',
            field=models.CharField(max_length=255, null=True),
        ),
        migrations.AddField(
            model_name='lcmtemp',
            name='collectionVehicleNo',
            field=models.CharField(max_length=255, null=True),
        ),
        migrations.AddField(
            model_name='lcmtemp',
            name='name',
            field=models.CharField(max_length=255, null=True),
        ),
        migrations.AddField(
            model_name='lcmtemp',
            name='sender_GST',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='lcmtemp',
            name='sender_address',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='lcmtemp',
            name='sender_mobile',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='lcm',
            name='lcm_no',
            field=models.CharField(max_length=50, null=True),
        ),
    ]
