# Generated by Django 4.1.2 on 2022-11-05 13:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('endpoints', '0022_alter_activities_options_alter_transactions_options_and_more'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='activities',
            options={'ordering': ['-id'], 'verbose_name_plural': 'Transactions'},
        ),
        migrations.AlterField(
            model_name='activities',
            name='createdOn',
            field=models.CharField(blank=True, default='05-11-2022 13:18:54', max_length=255, null=True),
        ),
        migrations.AlterField(
            model_name='request',
            name='createdOn',
            field=models.CharField(default='05-11-2022 13:18:54', max_length=255),
        ),
        migrations.AlterField(
            model_name='transactions',
            name='createdOn',
            field=models.CharField(default='05-11-2022 13:18:54', max_length=255),
        ),
        migrations.AlterField(
            model_name='users',
            name='createdOn',
            field=models.CharField(default='05-11-2022 13:18:54', max_length=255),
        ),
    ]
