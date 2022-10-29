# writing our serializer classes to
from rest_framework import serializers
from .models import Request, Users, Transactions, Documents


class DocumentsSerializer(serializers.ModelSerializer):
    user = serializers.StringRelatedField(many=False)

    class Meta:
        model = Documents
        fields = '__all__'


class UserSerializer(serializers.ModelSerializer):
    documents = DocumentsSerializer(many=True)

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
                  'ghanaCardNumber',
                  'isDeleted',
                  'documents'
                  )

    def create(self, validated_data):
        docuements_data = validated_data.pop('documents')
        user = Users.objects.create(**validated_data)

        for document in docuements_data:
            Documents.objects.create(user=user, **document)

        return user


class TransactionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Transactions
        fields = '__all__'


class RequestSerializer(serializers.ModelSerializer):
    class Meta:
        model = Request
        fields = '__all__'
