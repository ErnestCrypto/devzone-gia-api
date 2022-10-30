from django.contrib import admin
from .models import Users, Transactions, Request, Documents
# Register your models here.


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
        'email',
        'pin',
        'phoneNumber',
        'username',
        'memberType',
        'profileImage',
        'emailVerified',
        'status',
        'transactions',
        'requests',
        'transactionsMade',
        'totalInvestment',
        'withdrawalLimit',
        'withdrawalMade',
        'requestsMade',
        'isDeleted',

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
