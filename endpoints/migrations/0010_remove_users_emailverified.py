# Generated by Django 4.1.2 on 2022-11-03 20:25

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('endpoints', '0009_alter_address_user_alter_phonenumber_user'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='users',
            name='emailVerified',
        ),
    ]
