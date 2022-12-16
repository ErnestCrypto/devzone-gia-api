# building our api models
from django.db import models
from django.contrib.postgres.fields import ArrayField
import uuid
from .utils import custom_id, transaction_id
import datetime
from django.utils import timezone

TYPE = [("admin", "admin"), ("member", "member"), ("superadmin", "superadmin")]
MEMBER_TYPE = [("student", "student"), ("nonstudent", "nonstudent")]
STATUS = [("active", "active"), ("blocked", "blocked"), ("pending", "pending")]
TRANSACTION_TYPE = [("withdrawal", "withdrawal"), ("investment", "investment")]
STATUS = [("completed", "completed"),
          ("rejected", "rejected"), ("pending", "pending")]

# now = datetime.now()
# dt_string = now.strftime("%d-%m-%Y %H:%M:%S")


class Users(models.Model):
    memberId = models.CharField(
        primary_key=True, editable=False, unique=True, max_length=255, default=custom_id)
    firstname = models.CharField(max_length=255, default=None)
    lastname = models.CharField(max_length=255, default=None)
    type = models.CharField(max_length=255, default='member', choices=TYPE)
    dob = models.CharField(max_length=255, default=None)
    gender = models.CharField(max_length=255, default=None)
    createdOn = models.DateTimeField(default=timezone.now)
    pin = models.CharField(max_length=255, default=None)
    username = models.CharField(max_length=255, default=None)
    memberType = models.CharField(
        max_length=255, default=None, choices=MEMBER_TYPE)
    profileImage = models.CharField(
        max_length=255, default=None, blank=True, null=True)
    status = models.CharField(
        max_length=255, choices=STATUS, default='pending')
    transactions = models.TextField(blank=True, default='[]', null=True)
    requests = models.TextField(blank=True, default='[]', null=True)
    transactionsMade = models.CharField(max_length=255, default='0')
    totalInvestment = models.CharField(max_length=255, default='0')
    withdrawalLimit = models.CharField(max_length=255, default='2')
    withdrawalMade = models.CharField(max_length=255, default='0')
    requestsMade = models.CharField(max_length=255, default='0')
    isDeleted = models.BooleanField(default=False)
    isDeletedOn = models.DateTimeField(default=None, null=True, blank=True)
    expireDate = models.DateTimeField(default=None, null=True, blank=True)

    def __str__(self):
        return str(self.memberId)

    class Meta:
        ordering = ['-createdOn']
        verbose_name_plural = 'Users'


class Address(models.Model):
    user = models.OneToOneField(
        Users, related_name='address', on_delete=models.CASCADE)
    houseNumber = models.CharField(
        max_length=255, default=None)
    streetName = models.CharField(
        max_length=255, default=None)
    city = models.CharField(
        max_length=255, default=None)
    region = models.CharField(
        max_length=255, default=None)
    digitalAdress = models.CharField(
        max_length=255, default=None)

    def __str__(self):
        return str(self.id)

    class Meta:
        verbose_name_plural = 'Addresses'


class EmailAddress(models.Model):
    user = models.OneToOneField(
        Users, related_name='email', on_delete=models.CASCADE)
    type = models.CharField(
        max_length=255, default='secondary', null=True, blank=True)
    email = models.EmailField(default=None)
    isVerified = models.BooleanField(default=False)

    def __str__(self):
        return str(self.id)

    class Meta:
        verbose_name_plural = 'Emails'


class PhoneNumber(models.Model):
    user = models.ForeignKey(
        Users, related_name='phone', on_delete=models.CASCADE)
    type = models.CharField(
        max_length=255, default='secondary', null=True, blank=True)
    phoneNumber = models.CharField(
        max_length=255, default=None, null=True, blank=True)
    isVerified = models.BooleanField(default=False)

    def __str__(self):
        return str(self.id)

    class Meta:
        verbose_name_plural = 'Phone'


class Documents(models.Model):
    user = models.OneToOneField(
        Users, related_name='documents', on_delete=models.CASCADE)
    ghanaCardNumber = models.CharField(
        max_length=255, default=None)
    frontCardPic = models.CharField(
        max_length=255, default=None)
    backCardPic = models.CharField(
        max_length=255, default=None)

    def __str__(self):
        return str(self.id)

    class Meta:
        verbose_name_plural = 'Documents'


class Transactions(models.Model):
    transactionId = models.UUIDField(
        primary_key=True, default=uuid.uuid4, editable=False)
    transcationId = models.CharField(
        max_length=255, default=transaction_id, unique=True)
    createdBy = models.ForeignKey(
        Users, related_name="users_transactions", on_delete=models.CASCADE)
    type = models.CharField(max_length=255, default=None,
                            choices=TRANSACTION_TYPE)
    createdOn = models.DateTimeField(default=timezone.now)
    status = models.CharField(
        max_length=255, default='pending', choices=STATUS)
    amount = models.CharField(max_length=255, default='0.00')
    currency = models.CharField(max_length=255, default='GHS')

    def __str__(self):
        return str(self.transcationId)

    class Meta:
        ordering = ['createdOn']
        verbose_name_plural = 'Transactions'


class Request(models.Model):
    requestId = models.UUIDField(
        primary_key=True, default=uuid.uuid4, editable=False)
    createdOn = models.DateTimeField(default=timezone.now)
    updateOn = models.CharField(
        max_length=255, default=None, blank=True, null=True)
    status = models.CharField(
        max_length=255, choices=STATUS, default='pending')
    memberId = models.ForeignKey(
        Users, related_name='users_request', on_delete=models.CASCADE)
    amount = models.CharField(max_length=255, default='0.00')
    purpose = models.CharField(max_length=255, default=None)
    reason = models.CharField(max_length=255, default=None)
    type = models.CharField(max_length=255, default="business")
    isDeleted = models.BooleanField(default=False)

    def __str__(self):
        return str(self.requestId)


class Activities(models.Model):
    user = models.ForeignKey(
        Users, related_name='activities', on_delete=models.CASCADE, default=None, blank=True, null=True)
    name = models.CharField(
        max_length=255, default=None, blank=True, null=True)
    createdOn = models.DateTimeField(default=timezone.now)
    class Meta:
        ordering = ['-id']
        verbose_name_plural = 'Transactions'

    def __str__(self):
        return str(self.id)
