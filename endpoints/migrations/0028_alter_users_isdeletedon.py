# Generated by Django 4.1.2 on 2022-12-16 13:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('endpoints', '0027_users_deletetotally_alter_activities_createdon_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='users',
            name='isDeletedOn',
            field=models.DateTimeField(default=None),
        ),
    ]
