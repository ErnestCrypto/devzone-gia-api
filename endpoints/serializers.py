# writing our serializer classes to
from dataclasses import field
from rest_framework import serializers
from .models import Request, Users, Transactions, Documents, PhoneNumber, EmailAddress, Address, Activities


class ActivitiesSerializer(serializers.ModelSerializer):
    class Meta:
        model = Activities
        exclude = ('user',)


class GetActivitiesSerializer(serializers.ModelSerializer):
    class Meta:
        model = Activities
        fields = '__all__'


class EmailSerializer(serializers.ModelSerializer):
    class Meta:
        model = EmailAddress
        exclude = ('user',)


class UpdateEmailSerializer(serializers.ModelSerializer):
    class Meta:
        model = EmailAddress
        fields = '__all__'


class PhoneNumberSerializer(serializers.ModelSerializer):
    class Meta:
        model = PhoneNumber
        exclude = ('user',)


class UpdatePhoneNumberSerializer(serializers.ModelSerializer):
    class Meta:
        model = PhoneNumber
        fields = '__all__'


class AddressSerializer(serializers.ModelSerializer):
    class Meta:
        model = Address
        exclude = ('user',)


class UpdateAddressSerializer(serializers.ModelSerializer):
    class Meta:
        model = Address
        fields = '__all__'


class DocumentsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Documents
        exclude = ('user',)


class UpdateDocumentsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Documents
        fields = '__all__'


class PersonalDetails(serializers.ModelSerializer):
    class Meta:
        model = Users
        fields = '__all__'


class UserSerializer(serializers.ModelSerializer):
    email = EmailSerializer(many=False)
    documents = DocumentsSerializer(many=False)
    address = AddressSerializer(many=False)
    phone = PhoneNumberSerializer(many=True)
    activities = ActivitiesSerializer(many=True, required=False)

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
                  'activities',


                  )

    def create(self, validated_data):
        documents_data = validated_data.pop('documents')
        emails_data = validated_data.pop('email')
        address_data = validated_data.pop('address')
        phone_data = validated_data.pop('phone')

        user = Users.objects.create(**validated_data)
        Documents.objects.create(user=user, **documents_data)
        EmailAddress.objects.create(user=user, **emails_data)
        Address.objects.create(user=user, **address_data)
        for p_data in phone_data:
            PhoneNumber.objects.create(user=user, **p_data)

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
