# Generated by Django 4.1.2 on 2022-11-10 19:01

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('endpoints', '0026_users_isdeletedon_alter_activities_createdon_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='users',
            name='deleteTotally',
            field=models.IntegerField(default=30, null=True),
        ),
        migrations.AlterField(
            model_name='activities',
            name='createdOn',
            field=models.DateTimeField(default=django.utils.timezone.now),
        ),
        migrations.AlterField(
            model_name='request',
            name='createdOn',
            field=models.DateTimeField(default=django.utils.timezone.now),
        ),
        migrations.AlterField(
            model_name='transactions',
            name='createdOn',
            field=models.DateTimeField(default=django.utils.timezone.now),
        ),
        migrations.AlterField(
            model_name='users',
            name='createdOn',
            field=models.DateTimeField(default=django.utils.timezone.now),
        ),
        migrations.AlterField(
            model_name='users',
            name='isDeletedOn',
            field=models.DateTimeField(default=django.utils.timezone.now),
        ),
    ]
