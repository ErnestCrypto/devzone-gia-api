# writing our serializer classes to
from dataclasses import field
from rest_framework import serializers
from .models import Request, Users, Transactions, Documents


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
    documents = DocumentsSerializer(many=False)

    class Meta:
        model = Users
        fields = ('memberId',
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
                  'documents'
                  )

    def create(self, validated_data):
        documents_data = validated_data.pop('documents')
        user = Users.objects.create(**validated_data)
        Documents.objects.create(user=user, **documents_data)

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
