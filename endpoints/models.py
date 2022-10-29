# building our api models
from django.db import models
from django.contrib.postgres.fields import ArrayField
import uuid
from .utils import custom_id, transaction_id

TYPE = [("admin", "admin"), ("member", "member"), ("superadmin", "superadmin")]
MEMBER_TYPE = [("student", "student"), ("nonstudent", "nonstudent")]
STATUS = [("active", "active"), ("blocked", "blocked"), ("pending", "pending")]
TRANSACTION_TYPE = [("withdrawal", "withdrawal"), ("investment", "investment")]
STATUS = [("completed", "completed"),
          ("rejected", "rejected"), ("pending", "pending")]


class Users(models.Model):
    memberId = models.CharField(
        primary_key=True, editable=False, unique=True, max_length=255, default=custom_id)
    firstname = models.CharField(max_length=255, default=None)
    lastname = models.CharField(max_length=255, default=None)
    type = models.CharField(max_length=255, default='member', choices=TYPE)
    dob = models.CharField(max_length=255, default=None)
    gender = models.CharField(max_length=255, default=None)
    createdOn = models.DateTimeField(auto_now_add=True)
    email = models.EmailField(default=None)
    pin = models.CharField(max_length=255, default=None)
    phoneNumber = models.CharField(max_length=255, default=None)
    username = models.CharField(max_length=255, default=None)
    memberType = models.CharField(
        max_length=255, default=None, choices=MEMBER_TYPE)
    profileImage = models.CharField(
        max_length=255, default=None, blank=True, null=True)
    emailVerified = models.BooleanField(default=False, editable=False)
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

    def __str__(self):
        return str(self.memberId)

    class Meta:
        ordering = ['-createdOn']
        verbose_name_plural = 'Users'


class Documents(models.Model):
    user = models.ForeignKey(
        Users, related_name='documents', on_delete=models.CASCADE, null=True, blank=True)
    ghanaCardNumber = models.CharField(
        max_length=255, default=None, null=True, blank=True)
    frontCardPic = models.CharField(
        max_length=255, default=None, null=True, blank=True)
    backCardPic = models.CharField(
        max_length=255, default=None, null=True, blank=True)

    def __str__(self):
        self.id

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
    createdOn = models.DateTimeField(auto_now_add=True)
    status = models.CharField(
        max_length=255, default='pending', choices=STATUS)
    amount = models.CharField(max_length=255, default='0.00')
    currency = models.CharField(max_length=255, default='GHS')

    def __str__(self):
        return str(self.transcationId)


class Request(models.Model):
    requestId = models.UUIDField(
        primary_key=True, default=uuid.uuid4, editable=False)
    createdOn = models.DateTimeField(auto_now_add=True)
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
