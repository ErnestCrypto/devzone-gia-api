# Generated by Django 4.1.2 on 2022-10-26 14:05

from django.db import migrations, models
import django.db.models.deletion
import controllers.utils
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Users',
            fields=[
                ('memberId', controllers.CharField(default=controllers.utils.custom_id,
                 editable=False, max_length=255, primary_key=True, serialize=False, unique=True)),
                ('firstname', controllers.CharField(default=None, max_length=255)),
                ('lastname', controllers.CharField(default=None, max_length=255)),
                ('type', controllers.CharField(choices=[('admin', 'admin'), ('member', 'member'), (
                    'superadmin', 'superadmin')], default=None, max_length=255)),
                ('dob', controllers.CharField(default=None, max_length=255)),
                ('gender', controllers.CharField(default=None, max_length=255)),
                ('createdOn', controllers.DateTimeField(auto_now_add=True)),
                ('email', controllers.EmailField(default=None, max_length=254)),
                ('pin', controllers.CharField(default=None, max_length=255)),
                ('phoneNumber', controllers.CharField(
                    default=None, max_length=255)),
                ('username', controllers.CharField(default=None, max_length=255)),
                ('memberType', controllers.CharField(choices=[
                 ('student', 'student'), ('nonstudent', 'nonstudent')], default=None, max_length=255)),
                ('profileImage', controllers.CharField(
                    blank=True, default=None, max_length=255)),
                ('emailVerified', controllers.BooleanField(default=None)),
                ('status', controllers.CharField(choices=[('completed', 'completed'), (
                    'rejected', 'rejected'), ('pending', 'pending')], default=None, max_length=255)),
                ('transactions', controllers.TextField(blank=True, default=None)),
                ('requests', controllers.TextField(blank=True, default=None)),
                ('transactionsMade', controllers.CharField(
                    default='0', max_length=255)),
                ('totalInvestment', controllers.CharField(
                    default='0', max_length=255)),
                ('withdrawalLimit', controllers.CharField(
                    default='2', max_length=255)),
                ('withdrawalMade', controllers.CharField(
                    default='0', max_length=255)),
                ('requestsMade', controllers.CharField(
                    default='0', max_length=255)),
                ('ghanaCardNumber', controllers.CharField(
                    default=None, max_length=255)),
            ],
            options={
                'verbose_name_plural': 'Users',
                'ordering': ['createdOn'],
            },
        ),
        migrations.CreateModel(
            name='Transactions',
            fields=[
                ('id', controllers.UUIDField(default=uuid.uuid4,
                 editable=False, primary_key=True, serialize=False)),
                ('transcationId', controllers.CharField(
                    default=controllers.utils.transaction_id, max_length=255, unique=True)),
                ('type', controllers.CharField(choices=[
                 ('withdrawal', 'withdrawal'), ('investment', 'investment')], default=None, max_length=255)),
                ('createdOn', controllers.DateTimeField(auto_now_add=True)),
                ('status', controllers.CharField(choices=[('completed', 'completed'), (
                    'rejected', 'rejected'), ('pending', 'pending')], default=None, max_length=255)),
                ('amount', controllers.CharField(default='0.00', max_length=255)),
                ('currency', controllers.CharField(default='GHS', max_length=255)),
                ('createdBy', controllers.ForeignKey(on_delete=django.db.models.deletion.CASCADE,
                 related_name='users_transactions', to='giaApp.users')),
            ],
        ),
        migrations.CreateModel(
            name='Request',
            fields=[
                ('id', controllers.UUIDField(default=uuid.uuid4,
                 editable=False, primary_key=True, serialize=False)),
                ('createdOn', controllers.DateTimeField(auto_now_add=True)),
                ('updateOn', controllers.CharField(
                    blank=True, default=None, max_length=255, null=True)),
                ('status', controllers.CharField(choices=[('completed', 'completed'), (
                    'rejected', 'rejected'), ('pending', 'pending')], default=None, max_length=255)),
                ('amount', controllers.CharField(default='0.00', max_length=255)),
                ('purpose', controllers.CharField(default=None, max_length=255)),
                ('reason', controllers.CharField(default=None, max_length=255)),
                ('type', controllers.CharField(default='business', max_length=255)),
                ('isDeleted', controllers.BooleanField(default=False)),
                ('userId', controllers.ForeignKey(on_delete=django.db.models.deletion.CASCADE,
                 related_name='users_request', to='giaApp.users')),
            ],
        ),
    ]
