# Generated by Django 4.1.2 on 2022-11-02 14:09

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('endpoints', '0004_users_address_alter_users_email_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='documents',
            name='backCardPic',
            field=models.CharField(default=None, max_length=255),
        ),
        migrations.AlterField(
            model_name='documents',
            name='frontCardPic',
            field=models.CharField(default=None, max_length=255),
        ),
        migrations.AlterField(
            model_name='documents',
            name='ghanaCardNumber',
            field=models.CharField(default=None, max_length=255),
        ),
        migrations.CreateModel(
            name='UserPhoneNumber',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('type', models.CharField(blank=True, default=None, max_length=255, null=True)),
                ('userPhoneNumber', models.EmailField(default=None, max_length=254)),
                ('isVerified', models.BooleanField(default=False)),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='UserPhoneNumber', to='endpoints.users')),
            ],
            options={
                'verbose_name_plural': 'Phone',
            },
        ),
        migrations.CreateModel(
            name='UserEmailAddress',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('type', models.CharField(blank=True, default=None, max_length=255, null=True)),
                ('emailAddress', models.EmailField(default=None, max_length=254)),
                ('isVerified', models.BooleanField(default=False)),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='userEmail', to='endpoints.users')),
            ],
            options={
                'verbose_name_plural': 'Emails',
            },
        ),
        migrations.CreateModel(
            name='UserAddress',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('houseNumber', models.CharField(default=None, max_length=255)),
                ('streetName', models.CharField(default=None, max_length=255)),
                ('city', models.CharField(default=None, max_length=255)),
                ('region', models.CharField(default=None, max_length=255)),
                ('digitalAdress', models.CharField(default=None, max_length=255)),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='userAddress', to='endpoints.users')),
            ],
            options={
                'verbose_name_plural': 'Addresses',
            },
        ),
    ]