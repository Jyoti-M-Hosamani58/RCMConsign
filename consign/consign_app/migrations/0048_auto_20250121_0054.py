# Generated by Django 3.0 on 2025-01-20 19:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('consign_app', '0047_auto_20250120_2334'),
    ]

    operations = [
        migrations.RenameField(
            model_name='delcharge',
            old_name='rate',
            new_name='delrate',
        ),
        migrations.RenameField(
            model_name='pickcharge',
            old_name='rate',
            new_name='pickrate',
        ),
        migrations.AlterField(
            model_name='client',
            name='GST',
            field=models.CharField(max_length=500, null=True),
        ),
        migrations.AlterField(
            model_name='client',
            name='address',
            field=models.CharField(max_length=500, null=True),
        ),
        migrations.AlterField(
            model_name='client',
            name='city',
            field=models.CharField(max_length=500, null=True),
        ),
        migrations.AlterField(
            model_name='client',
            name='clientType',
            field=models.CharField(max_length=500, null=True),
        ),
        migrations.AlterField(
            model_name='client',
            name='email',
            field=models.CharField(max_length=500, null=True),
        ),
        migrations.AlterField(
            model_name='client',
            name='foc',
            field=models.CharField(max_length=500, null=True),
        ),
        migrations.AlterField(
            model_name='client',
            name='mobile',
            field=models.CharField(max_length=500, null=True),
        ),
        migrations.AlterField(
            model_name='client',
            name='name',
            field=models.CharField(max_length=500, null=True),
        ),
        migrations.AlterField(
            model_name='client',
            name='pickup',
            field=models.CharField(max_length=500, null=True),
        ),
        migrations.AlterField(
            model_name='client',
            name='pincode',
            field=models.CharField(max_length=500, null=True),
        ),
        migrations.AlterField(
            model_name='client',
            name='tbb',
            field=models.CharField(max_length=500, null=True),
        ),
        migrations.AlterField(
            model_name='client',
            name='telephone',
            field=models.CharField(max_length=500, null=True),
        ),
        migrations.AlterField(
            model_name='client',
            name='thirdParty',
            field=models.CharField(max_length=500, null=True),
        ),
        migrations.AlterField(
            model_name='incharge',
            name='inchargeEmail',
            field=models.CharField(max_length=500, null=True),
        ),
        migrations.AlterField(
            model_name='incharge',
            name='inchargeName',
            field=models.CharField(max_length=500, null=True),
        ),
        migrations.AlterField(
            model_name='incharge',
            name='inchargePhone',
            field=models.IntegerField(null=True),
        ),
        migrations.AlterField(
            model_name='incharge',
            name='inchargeRole',
            field=models.CharField(max_length=500, null=True),
        ),
    ]
