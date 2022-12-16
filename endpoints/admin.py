from django.contrib import admin
from .models import Users, Transactions, Request, Documents, PhoneNumber, EmailAddress, Address, Activities
# Register your models here.


@admin.register(PhoneNumber)
class PhoneNumberAdmin(admin.ModelAdmin):
    list_display = ['user',
                    'type',
                    'phoneNumber',
                    'isVerified'
                    ]


@admin.register(EmailAddress)
class EmailAdressAdmin(admin.ModelAdmin):
    list_display = ['user',
                    'type',
                    'email',
                    'isVerified'
                    ]


@admin.register(Address)
class AddressAdmin(admin.ModelAdmin):
    list_display = ['user',
                    'houseNumber',
                    'streetName',
                    'city',
                    'region',
                    'digitalAdress'
                    ]


@admin.register(Users)
class UserAdmin(admin.ModelAdmin):
    list_display = [

        'memberId',
        'firstname',
        'lastname',
        'type',
        'dob',
        'gender',
        'createdOn',
        'pin',
        'username',
        'memberType',
        'profileImage',
        'status',
        'transactions',
        'requests',
        'transactionsMade',
        'totalInvestment',
        'withdrawalLimit',
        'withdrawalMade',
        'requestsMade',
        'isDeleted',
        'isDeletedOn',
        'expireDate',

    ]


@admin.register(Documents)
class DocumentsAdmin(admin.ModelAdmin):
    list_display = ['user',
                    'ghanaCardNumber',
                    'frontCardPic',
                    'backCardPic',
                    ]


@admin.register(Transactions)
class TransactionsAdmin(admin.ModelAdmin):
    list_display = ['transactionId',
                    'transcationId',
                    'type',
                    'createdOn',
                    'status',
                    'amount',
                    'currency',
                    ]


@admin.register(Request)
class RequestAdmin(admin.ModelAdmin):
    list_display = ['requestId',
                    'createdOn',
                    'updateOn',
                    'status',
                    'memberId',
                    'amount',
                    'purpose',
                    'reason',
                    'type',
                    'isDeleted',
                    ]


@admin.register(Activities)
class ActivitiesAdmin(admin.ModelAdmin):
    list_display = ['id',
                    'user',
                    'createdOn',
                    'name', ]
