# Generated by Django 4.1.2 on 2022-11-02 14:25

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('endpoints', '0005_alter_documents_backcardpic_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='users',
            name='address',
        ),
        migrations.RemoveField(
            model_name='users',
            name='email',
        ),
        migrations.RemoveField(
            model_name='users',
            name='phoneNumber',
        ),
    ]