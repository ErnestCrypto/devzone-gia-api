# Generated by Django 4.1.2 on 2022-11-05 11:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('endpoints', '0016_activities_createdon_activities_name_activities_user_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='activities',
            name='createdOn',
            field=models.CharField(default='05-11-2022 11:23:54', max_length=255),
        ),
        migrations.AlterField(
            model_name='request',
            name='createdOn',
            field=models.CharField(default='05-11-2022 11:23:54', max_length=255),
        ),
        migrations.AlterField(
            model_name='transactions',
            name='createdOn',
            field=models.CharField(default='05-11-2022 11:23:54', max_length=255),
        ),
        migrations.AlterField(
            model_name='users',
            name='createdOn',
            field=models.CharField(default='05-11-2022 11:23:54', max_length=255),
        ),
    ]
