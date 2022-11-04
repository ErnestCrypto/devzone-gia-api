# creating our API views here
from django.shortcuts import render
from . import models
from . import serializers
from django.http import Http404
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from datetime import datetime


class UsersList(APIView):
    "List all the users or create a new user"

    def get(self, request, format=None):
        users = models.Users.objects.filter(isDeleted=False)
        serializer = serializers.UserSerializer(users, many=True)
        return Response(serializer.data)

    def post(self, request, format=None):
        serializer = serializers.UserSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class UsersById(APIView):
    "get users by memberId"

    def get_object(self, userId):
        try:
            user = models.Users.objects.get(memberId=userId)
            if user.isDeleted == False:
                return user
            else:
                raise Http404
        except models.Users.DoesNotExist:
            raise Http404

    def get(self, request, userId, format=None):
        users = self.get_object(userId)
        serializer = serializers.UserSerializer(users)
        return Response(serializer.data)


class DeleteUser(APIView):
    "delete users by memberId"

    def get_object(self, userId):
        try:
            user = models.Users.objects.get(memberId=userId)
            if user.isDeleted == False:
                return user
            else:
                raise Exception("User already deleted")
        except models.Users.DoesNotExist:
            raise Http404

    def put(self, request, userId, format=None):
        users = self.get_object(userId)
        users.isDeleted = True
        users.save()
        serializer = serializers.UserSerializer(users)
        return Response(serializer.data)


class RecoverUser(APIView):
    "delete users by memberId"

    def get_object(self, userId):
        try:
            user = models.Users.objects.get(memberId=userId)
            if user.isDeleted == True:
                return user
            else:
                raise Exception("User not deleted")
        except models.Users.DoesNotExist:
            raise Http404

    def put(self, request, userId, format=None):
        users = self.get_object(userId)
        users.isDeleted = False
        users.save()
        serializer = serializers. UserSerializer(users)
        return Response(serializer.data)


class UpdatePin(APIView):
    "update a users pin"

    def get_object(self, userId):
        try:
            user = models.Users.objects.get(memberId=userId)
            if user.isDeleted == False:
                return user
            else:
                raise Http404
        except models.Users.DoesNotExist:
            raise Http404

    def put(self, request, userId, format=None):
        users = self.get_object(userId)
        serializer = serializers.PersonalDetails(data=request.data)
        if serializer.is_valid():

            try:
                users.pin = request.data['pin']
                users.save()

            except:
                Exception("Could not save")
        else:
            Exception("Invalid data")
        serializer = serializers.UserSerializer(users)
        return Response(serializer.data)


class UpdateEmail(APIView):
    "update a users Email"

    def get_email(self, userId):
        try:
            user = models.Users.objects.get(memberId=userId)
            if user.isDeleted == False:
                email = models.EmailAddress.objects.get(user=userId)
                return email
            else:
                raise Http404
        except models.Users.DoesNotExist:
            raise Http404

    def put(self, request, userId, format=None):
        email = self.get_email(userId)
        serializer = serializers.EmailSerializer(email, data=request.data)
        if serializer.is_valid():
            try:
                email.type = request.data['type']
                email.email = request.data['email']
                email.save()
            except:
                raise Exception("Could not save")
        else:
            raise Exception("Invalid data")
        serializer = serializers.UpdateEmailSerializer(email)
        return Response(serializer.data)


class UpdateUserPhoneNumber(APIView):
    "update a users phone number"

    def get_object(self, userId, phoneId):
        try:
            user = models.Users.objects.get(memberId=userId)
            if user.isDeleted == False:
                phone = models.PhoneNumber.objects.get(id=phoneId)
                return phone
            else:
                raise Http404
        except models.Users.DoesNotExist:
            raise Http404

    def put(self, request, userId, phoneId, format=None):
        phone = self.get_object(userId, phoneId)
        serializer = serializers.PhoneNumberSerializer(
            phone, data=request.data)
        if serializer.is_valid():
            try:
                phone.phoneNumber = request.data['phoneNumber']
                phone.type = request.data['type']
                phone.save()
            except:
                Exception("Could not save")
        else:
            Exception("Invalid data")
        serializer = serializers.UpdatePhoneNumberSerializer(phone)
        return Response(serializer.data)


class UpdateUserAddress(APIView):
    "update a users phone number"

    def get_object(self, userId):
        try:
            user = models.Users.objects.get(memberId=userId)
            if user.isDeleted == False:
                address = models.Address.objects.get(user=userId)
                return address
            else:
                raise Http404
        except models.Users.DoesNotExist:
            raise Http404

    def put(self, request, userId, format=None):
        address = self.get_object(userId)
        serializer = serializers.AddressSerializer(
            address, data=request.data)
        if serializer.is_valid():
            try:
                address.houseNumber = request.data['houseNumber']
                address.streetName = request.data['streetName']
                address.city = request.data['city']
                address.region = request.data['region']
                address.digitalAdress = request.data['digitalAdress']
                address.save()
            except:
                Exception("Could not save")
        else:
            Exception("Invalid data")
        serializer = serializers.UpdateAddressSerializer(address)
        return Response(serializer.data)


class UpdateUser(APIView):
    "update a users pin"

    def get_object(self, userId):
        try:
            user = models.Users.objects.get(memberId=userId)
            if user.isDeleted == False:
                return user
            else:
                raise Http404
        except models.Users.DoesNotExist:
            raise Http404

    def put(self, request, userId, format=None):
        users = self.get_object(userId)
        serializer = serializers.PersonalDetails(
            data=request.data)
        if serializer.is_valid():
            try:
                users.firstname = request.data['firstname']
                users.lastname = request.data['lastname']
                users.dob = request.data['dob']
                users.gender = request.data['gender']
                users.memberType = request.data['memberType']
                users.profileImage = request.data['profileImage']
                users.save()
            except:
                raise Exception('Could not save')
        else:
            raise Exception("Invalid data")
        serializer = serializers.UserSerializer(users)
        return Response(serializer.data)


class UpdateUserDocuments(APIView):
    "update a users documents"

    def get_document(self, userId):
        try:
            user = models.Users.objects.get(memberId=userId)
            if user.isDeleted == False:
                document = models.Documents.objects.get(user=userId)
                return document
            else:
                raise Http404
        except models.Users.DoesNotExist:
            raise Http404

    def put(self, request, userId, format=None):
        document = self.get_document(userId)
        serializer = serializers.DocumentsSerializer(
            document, data=request.data)
        if serializer.is_valid():
            try:
                document.ghanaCardNumber = request.data['ghanaCardNumber']
                document.frontCardPic = request.data['frontCardPic']
                document.backCardPic = request.data['backCardPic']
                document.save()
            except:
                raise Exception('Could not save')
        else:
            raise Exception("Invalid data")
        serializer = serializers.UpdateDocumentsSerializer(document)
        return Response(serializer.data)


class RequestList(APIView):
    def get_user(self, request):
        try:
            user = models.Users.objects.get(memberId=request.data['memberId'])
            if user.isDeleted == False:
                return user
            else:
                raise Http404
        except models.Users.DoesNotExist:
            raise Http404

    def get(self, request, format=None):
        requests = models.Request.objects.filter(isDeleted=False)
        serializer = serializers.RequestSerializer(requests, many=True)
        return Response(serializer.data)

    def post(self, request, format=None):
        serializer = serializers.RequestSerializer(data=request.data)
        user = self.get_user(request)
        if serializer.is_valid():
            serializer.save()
            filtered_requests = models.Request.objects.filter(
                memberId=user.memberId, isDeleted=False)
            array = []
            for filtered_request in filtered_requests:
                array.append(filtered_request)
            user.requests = array
            user.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class RequestById(APIView):
    "get a request by Id"

    def get_object(self, requestId):
        try:
            request_obeject = models.Request.objects.get(
                requestId=requestId)
            if request_obeject.isDeleted == False:
                return request_obeject
            else:
                raise Http404
        except models.Request.DoesNotExist:
            raise Http404

    def get(self, request, requestId, format=None):
        request_object = self.get_object(requestId)
        serializer = serializers.RequestSerializer(request_object)
        return Response(serializer.data)


class UpdateRequest(APIView):
    def get_object(self, requestId):
        try:
            request_obeject = models.Request.objects.get(
                requestId=requestId)
            if request_obeject.isDeleted == False:
                return request_obeject
            else:
                raise Http404
        except models.Request.DoesNotExist:
            raise Http404

    def get_user(self, requestId):
        try:
            request_object = self.get_object(requestId)
            user = models.Users.objects.get(memberId=request_object.memberId)
            if user.isDeleted == False:
                return user
            else:
                raise Exception("This user has been deleted")
        except models.Users.DoesNotExist:
            raise Exception("Sorry User details not found")

    def put(self, request, requestId, format=None):
        request_object = self.get_object(requestId)
        serializer = serializers.UpdateRequestSerializer(data=request.data)
        user = self.get_user(requestId)
        now = datetime.now()
        dt_string = now.strftime("%d-%m-%Y %H:%M:%S")
        if serializer.is_valid():
            try:
                request_object.updateOn = dt_string
                request_object.status = request.data['status']
                request_object.amount = request.data['amount']
                request_object.purpose = request.data['purpose']
                request_object.reason = request.data['reason']
                request_object.type = request.data['type']
                request_object.save()
            except:
                raise Exception('Could not save')
            filtered_requests = models.Request.objects.filter(
                memberId=user.memberId, isDeleted=False)
            array_request = []
            for filtered_request in filtered_requests:
                array_request.append(filtered_request.requestId)
            user.requests = array_request
            user.save()
            serializer = serializers.RequestSerializer(request_object)
        else:
            raise Exception('invalid data')
        return Response(serializer.data)


class DeleteRequest(APIView):
    "delete request"

    def get_object(self, requestId):
        try:
            request_obeject = models.Request.objects.get(
                requestId=requestId)
            if request_obeject.isDeleted == False:
                return request_obeject
            else:
                raise Http404
        except models.Request.DoesNotExist:
            raise Http404

    def get_user(self, requestId):
        try:
            request_object = self.get_object(requestId)
            user = models.Users.objects.get(memberId=request_object.memberId)
            if user.isDeleted == False:
                return user
            else:
                raise Http404
        except models.Users.DoesNotExist:
            raise Http404

    def put(self, request, requestId, format=None):
        request_object = self.get_object(requestId)
        request_object.isDeleted = True
        request_object.save()
        user = self.get_user(requestId)
        filtered_requests = models.Request.objects.filter(
            memberId=user.memberId, isDeleted=False)
        array_request = []
        for filtered_request in filtered_requests:
            array_request.append(filtered_request.requestId)
        user.requests = array_request
        user.save()
        serializer = serializers.RequestSerializer(request_object)
        return Response(serializer.data)
