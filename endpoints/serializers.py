# writing our serializer classes to
from dataclasses import field
from rest_framework import serializers
from .models import Request, Users, Transactions, Documents, PhoneNumber, EmailAddress, Address


class EmailSerializer(serializers.ModelSerializer):
    class Meta:
        model = EmailAddress
        fields = (
            'type',
            'email'
        )


class PhoneNumberSerializer(serializers.ModelSerializer):
    class Meta:
        model = PhoneNumber
        fields = ('type',
                  'phoneNumber')


class AddressSerializer(serializers.ModelSerializer):
    class Meta:
        model = Address
        fields = ('houseNumber',
                  'streetName',
                  'city',
                  'region',
                  'digitalAdress')


class DocumentsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Documents
        fields = ('ghanaCardNumber',
                  'frontCardPic',
                  'backCardPic',)


class PersonalDetails(serializers.ModelSerializer):
    class Meta:
        model = Users
        fields = '__all__'


class UserSerializer(serializers.ModelSerializer):
    email = EmailSerializer(many=False)
    documents = DocumentsSerializer(many=False)
    phone = PhoneNumberSerializer(many=True)
    address = AddressSerializer(many=True)

    class Meta:
        model = Users
        fields = ('memberId',
                  'firstname',
                  'lastname',
                  'type',
                  'dob',
                  'gender',
                  'createdOn',
                  'pin',
                  'email',
                  'phone',
                  'address',
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
                  'documents',


                  )

    def create(self, validated_data):
        documents_data = validated_data.pop('documents')
        emails_data = validated_data.pop('email')
        address_data = validated_data.pop('address')
        phone_data = validated_data.pop('phone')

        user = Users.objects.create(**validated_data)
        Documents.objects.create(user=user, **documents_data)
        EmailAddress.objects.create(user=user, **emails_data)

        for p_data in phone_data:
            PhoneNumber.objects.create(user=user, **p_data)
        for a_data in address_data:
            Address.objects.create(user=user, **a_data)

        return user


class TransactionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Transactions
        fields = '__all__'


class RequestSerializer(serializers.ModelSerializer):

    class Meta:
        model = Request
        fields = '__all__'


class UpdateRequestSerializer(serializers.ModelSerializer):
    class Meta:
        model = Request
        exclude = ('memberId',)
