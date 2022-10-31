# creating our API views here
import re
from django.shortcuts import render
from .models import Users, Transactions, Request, Documents
from .serializers import UserSerializer, TransactionSerializer, RequestSerializer, PersonalDetails
from django.http import Http404
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status


class UsersList(APIView):
    "List all the users or create a new user"

    def get(self, request, format=None):
        users = Users.objects.filter(isDeleted=False)
        serializer = UserSerializer(users, many=True)
        return Response(serializer.data)

    def post(self, request, format=None):
        serializer = UserSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class UsersById(APIView):
    "get users by memberId"

    def get_object(self, request):
        try:
            user = Users.objects.get(memberId=request.data['memberId'])
            if user.isDeleted == False:
                return user
            else:
                raise Http404
        except Users.DoesNotExist:
            raise Http404

    def post(self, request, format=None):
        users = self.get_object(request)
        serializer = UserSerializer(users)
        return Response(serializer.data)


class DeleteUser(APIView):
    "delete users by memberId"

    def get_object(self, request):
        try:
            user = Users.objects.get(memberId=request.data['memberId'])
            if user.isDeleted == False:
                return user
            else:
                raise Http404
        except Users.DoesNotExist:
            raise Http404

    def put(self, request, format=None):
        users = self.get_object(request)
        users.isDeleted = True
        users.save()
        serializer = UserSerializer(users)
        return Response(serializer.data)


class UpdatePin(APIView):
    "update a users pin"

    def get_object(self, request):
        try:
            user = Users.objects.get(memberId=request.data['memberId'])
            if user.isDeleted == False:
                return user
            else:
                raise Http404
        except Users.DoesNotExist:
            raise Http404

    def put(self, request, format=None):
        users = self.get_object(request)
        serializer = PersonalDetails(data=request.data)
        if serializer.is_valid():
            try:
                users.pin = request.data['pin']
                users.save()

            except:
                Exception("Could not save")
        else:
            Exception("Invalid data")
        serializer = UserSerializer(users)
        return Response(serializer.data)


class UpdateEmail(APIView):
    "update a users Email"

    def get_object(self, request):
        try:
            user = Users.objects.get(memberId=request.data['memberId'])
            if user.isDeleted == False:
                return user
            else:
                raise Http404
        except Users.DoesNotExist:
            raise Http404

    def put(self, request, format=None):
        users = self.get_object(request)
        serializer = PersonalDetails(data=request.data)
        if serializer.is_valid():
            try:

                users.email = request.data['email']
                users.save()

            except:
                Exception("Could not save")
        else:
            Exception("Invalid data")
        serializer = UserSerializer(users)
        return Response(serializer.data)


class UpdateUserPhoneNumber(APIView):
    "update a users phone number"

    def get_object(self, request):
        try:
            user = Users.objects.get(memberId=request.data['memberId'])
            if user.isDeleted == False:
                return user
            else:
                raise Http404
        except Users.DoesNotExist:
            raise Http404

    def put(self, request, format=None):
        users = self.get_object(request)
        serializer = PersonalDetails(data=request.data)
        if serializer.is_valid():
            try:

                users.phoneNumber = request.data['phoneNumber']
                users.save()

            except:
                Exception("Could not save")
        else:
            Exception("Invalid data")
        serializer = UserSerializer(users)
        return Response(serializer.data)


class UpdateUser(APIView):
    "update a users pin"

    def get_object(self, request):
        try:
            user = Users.objects.get(memberId=request.data['memberId'])
            if user.isDeleted == False:
                return user
            else:
                raise Http404
        except Users.DoesNotExist:
            raise Http404

    def put(self, request, format=None):
        users = self.get_object(request)
        serializer = PersonalDetails(
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
        serializer = UserSerializer(users)
        return Response(serializer.data)


class UpdateUserDocuments(APIView):
    "update a users documents"

    def get_object(self, request):
        try:
            user = Users.objects.get(memberId=request.data['memberId'])
            if user.isDeleted == False:
                return user
            else:
                raise Http404
        except Users.DoesNotExist:
            raise Http404

    def get_document(self, request):
        try:
            user = self.get_object(request)
            if user.isDeleted == False:
                document = Documents.objects.get(user=request.data['memberId'])
                return document
            else:
                raise Http404
        except Users.DoesNotExist:
            raise Http404

    def put(self, request, format=None):
        document = self.get_document(request)
        users = self.get_object(request)
        serializer = UserSerializer(data=request.data)
        if serializer.is_valid():
            document.ghanaCardNumber = request.data['documents']['ghanaCardNumber']
            document.frontCardPic = request.data['documents']['frontCardPic']
            document.backCardPic = request.data['documents']['backCardPic']
            document.save()
        else:
            Exception("Invalid data")
        serializer = UserSerializer(users)
        return Response(serializer.data)


class RequestList(APIView):
    def get_user(self, request):
        try:
            user = Users.objects.get(memberId=request.data['memberId'])
            if user.isDeleted == False:
                return user
            else:
                raise Http404
        except Users.DoesNotExist:
            raise Http404

    def get(self, request, format=None):
        requests = Request.objects.filter(isDeleted=False)
        serializer = RequestSerializer(requests, many=True)
        return Response(serializer.data)

    def post(self, request, format=None):
        serializer = RequestSerializer(data=request.data)
        user = self.get_user(request)
        if serializer.is_valid():
            serializer.save()
            filtered_requests = Request.objects.filter(
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

    def get_object(self, request):
        try:
            request_obeject = Request.objects.get(
                requestId=request.data['requestId'])
            if request_obeject.isDeleted == False:
                return request_obeject
            else:
                raise Http404
        except Request.DoesNotExist:
            raise Http404

    def post(self, request, format=None):
        request_object = self.get_object(request)
        serializer = RequestSerializer(request_object)
        return Response(serializer.data)


class UpdateRequest(APIView):
    def get_object(self, request):
        try:
            request_obeject = Request.objects.get(
                requestId=request.data['requestId'])
            if request_obeject.isDeleted == False:
                return request_obeject
            else:
                raise Http404
        except Request.DoesNotExist:
            raise Http404

    def get_user(self, request):
        try:
            request_object = self.get_object(request)
            user = Users.objects.get(memberId=request_object.memberId)
            if user.isDeleted == False:
                return user
            else:
                raise("This user has been deleted")
        except Users.DoesNotExist:
            raise("Sorry User details not found")

    def put(self, request, format=None):
        request_object = self.get_object(request)
        serializer = RequestSerializer(data=request.data)
        if serializer.is_valid():
            try:
                request_object.status = request.data['status']
                request_object.amount = request.data['amount']
                request_object.purpose = request.data['purpose']
                request_object.reason = request.data['reason']
                request_object.type = request.data['type']
                request_object.save()
                user = self.get_user(request)
            except:
                raise Exception('Could not save')
            filtered_requests = Request.objects.filter(
                memberId=user.memberId, isDeleted=False)
            array_request = []
            for filtered_request in filtered_requests:
                array_request.append(filtered_request.requestId)
            user.requests = array_request
            user.save()
        serializer = RequestSerializer(user)
        return Response(serializer.data)


class DeleteRequest(APIView):
    "delete request"

    def get_object(self, request):
        try:
            request_obeject = Request.objects.get(
                requestId=request.data['requestId'])
            if request_obeject.isDeleted == False:
                return request_obeject
            else:
                raise Http404
        except Request.DoesNotExist:
            raise Http404

    def get_user(self, request):
        try:
            request_object = self.get_object(request)
            user = Users.objects.get(memberId=request_object.memberId)
            if user.isDeleted == False:
                return user
            else:
                raise Http404
        except Users.DoesNotExist:
            raise Http404

    def put(self, request, format=None):
        request_object = self.get_object(request)
        request_object.isDeleted = True
        request_object.save()
        user = self.get_user(request)
        filtered_requests = Request.objects.filter(
            memberId=user.memberId, isDeleted=False)
        array_request = []
        for filtered_request in filtered_requests:
            array_request.append(filtered_request.requestId)
        user.requests = array_request
        user.save()
        serializer = RequestSerializer(request_object)
        return Response(serializer.data)
