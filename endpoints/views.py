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
            try:
                serializer.save()
                return Response(serializer.data, status=status.HTTP_201_CREATED)
            except:
                raise Exception('Could not create user')

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
        try:
            users.isDeleted = True
            users.save()
            activities = models.Activities.objects.create(
                user=users, name='Deleted User Account successfully')
            activities.save()
            serializer = serializers.UserSerializer(users)
            return Response(serializer.data)
        except:
            activities = models.Activities.objects.create(
                user=users, name='Failed to delete user account')
            activities.save()
            raise Exception("could not delete user")


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
        try:
            users.isDeleted = False
            users.save()
            activities = models.Activities.objects.create(
                user=users, name='Recovered account successfully')
            activities.save()
            serializer = serializers. UserSerializer(users)
            return Response(serializer.data)
        except:
            activities = models.Activities.objects.create(
                user=users, name='Failed to recover account')
            activities.save()
            raise Exception('could not recover account')


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
                activities = models.Activities.objects.create(
                    user=users, name='Updated user pin successfully')
                activities.save()

            except:
                activities = models.Activities.objects.create(
                    user=users, name='Failed to update user pin')
                activities.save()
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
        users = models.Users.objects.get(memberId=userId)
        serializer = serializers.EmailSerializer(email, data=request.data)
        if serializer.is_valid():
            try:
                email.type = request.data['type']
                email.email = request.data['email']
                email.save()
                activities = models.Activities.objects.create(
                    user=users, name='Updated user email successfully')
                activities.save()
            except:
                activities = models.Activities.objects.create(
                    user=users, name='Failed to update user email')
                activities.save()
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

        users = models.Users.objects.get(memberId=userId)
        serializer = serializers.PhoneNumberSerializer(
            phone, data=request.data)
        if serializer.is_valid():
            try:
                phone.phoneNumber = request.data['phoneNumber']
                phone.type = request.data['type']
                phone.save()
                activities = models.Activities.objects.create(
                    user=users, name='Updated user phone number successfully')
                activities.save()
            except:
                activities = models.Activities.objects.create(
                    user=users, name='Failed to update user phone number')
                activities.save()
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
        users = models.Users.objects.get(memberId=userId)
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
                activities = models.Activities.objects.create(
                    user=users, name='Updated user address successfully')
                activities.save()
            except:
                activities = models.Activities.objects.create(
                    user=users, name='Failed to update user address')
                activities.save()
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
                activities = models.Activities.objects.create(
                    user=users, name='Updated user account successfully')
                activities.save()
            except:
                activities = models.Activities.objects.create(
                    user=users, name='Failed to update user account')
                activities.save()
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
        users = models.Users.objects.get(memberId=userId)
        serializer = serializers.DocumentsSerializer(
            document, data=request.data)
        if serializer.is_valid():
            try:
                document.ghanaCardNumber = request.data['ghanaCardNumber']
                document.frontCardPic = request.data['frontCardPic']
                document.backCardPic = request.data['backCardPic']
                document.save()
                activities = models.Activities.objects.create(
                    user=users, name='Updated user documents successfully')
                activities.save()
            except:
                activities = models.Activities.objects.create(
                    user=users, name='Failed to update user documents')
                activities.save()
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
            try:
                serializer.save()
                filtered_requests = models.Request.objects.filter(
                    memberId=user.memberId, isDeleted=False)
                array = []
                for filtered_request in filtered_requests:
                    array.append(filtered_request)
                user.requests = array
                user.save()
                activities = models.Activities.objects.create(
                    user=user, name='Made a request successfully')
                activities.save()
                return Response(serializer.data, status=status.HTTP_201_CREATED)
            except:
                activities = models.Activities.objects.create(
                    user=user, name='Request failed')
                activities.save()
                raise Exception('Could not make the request')
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
                filtered_requests = models.Request.objects.filter(
                    memberId=user.memberId, isDeleted=False)
                array_request = []
                for filtered_request in filtered_requests:
                    array_request.append(filtered_request.requestId)
                user.requests = array_request
                user.save()
                serializer = serializers.RequestSerializer(request_object)
                activities = models.Activities.objects.create(
                    user=user, name='Update request successfully')
                activities.save()
            except:
                activities = models.Activities.objects.create(
                    user=user, name='Failed to update request')
                activities.save()
                raise Exception('Could not save')

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
        user = self.get_user(requestId)
        try:
            request_object.isDeleted = True
            request_object.save()

            filtered_requests = models.Request.objects.filter(
                memberId=user.memberId, isDeleted=False)
            array_request = []
            for filtered_request in filtered_requests:
                array_request.append(filtered_request.requestId)
            user.requests = array_request
            user.save()
            activities = models.Activities.objects.create(
                user=user, name='Deleted request successfully')
            activities.save()
            serializer = serializers.RequestSerializer(request_object)
            return Response(serializer.data)
        except:
            activities = models.Activities.objects.create(
                user=user, name='Failed to delete request')
            activities.save()
            raise Exception('could not delete request')


class ActivityById(APIView):
    "get a request by Id"

    def get_object(self, activityId):
        try:
            activity_object = models.Activities.objects.get(
                id=activityId)
            return activity_object
        except models.Activities.DoesNotExist:
            raise Http404

    def get(self, request, activityId, format=None):
        activity_object = self.get_object(activityId)
        serializer = serializers.GetActivitiesSerializer(activity_object)
        return Response(serializer.data)


class UserActivityById(APIView):
    "get a request by Id"

    def get_object(self, userId):
        try:
            activity_objects = models.Activities.objects.filter(
                user=userId)
            return activity_objects
        except models.Activities.DoesNotExist:
            raise Http404

    def get(self, request, userId, format=None):
        activity_objects = self.get_object(userId)
        serializer = serializers.GetActivitiesSerializer(
            activity_objects, many=True)
        return Response(serializer.data)
