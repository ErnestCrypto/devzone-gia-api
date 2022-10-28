# creating our API views here
import re
from django.shortcuts import render
from .models import Users, Transactions, Request
from .serializers import UserSerializer, TransactionSerializer, RequestSerializer
from django.http import Http404
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from django.contrib import messages


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
            return Users.objects.get(memberId=request.data['memberId'])
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
            return Users.objects.get(memberId=request.data['memberId'])
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
            return Users.objects.get(memberId=request.data['memberId'])
        except Users.DoesNotExist:
            raise Http404

    def put(self, request, format=None):
        users = self.get_object(request)
        new_pin = request.data['pin']
        users.pin = new_pin
        users.save()
        serializer = UserSerializer(users)
        return Response(serializer.data)


class RequestList(APIView):
    def get(self, request, format=None):
        requests = Request.objects.filter(isDeleted=False)
        serializer = RequestSerializer(requests, many=True)
        return Response(serializer.data)

    def post(self, request, format=None):
        serializer = RequestSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class RequestById(APIView):
    "get a request by Id"

    def get_object(self, request):
        try:
            request_obeject = Request.objects.get(
                requestId=request.data['requestId'])
            return request_obeject
        except Request.DoesNotExist:
            raise Http404

    def post(self, request, format=None):
        request_object = self.get_object(request)
        serializer = RequestSerializer(request_object)
        return Response(serializer.data)


class DeleteRequest(APIView):
    "delete request"

    def get_object(self, request):
        try:
            request_obeject = Request.objects.get(
                requestId=request.data['requestId'])
            return request_obeject
        except Request.DoesNotExist:
            raise Http404

    def put(self, request, format=None):
        request_object = self.get_object(request)
        request_object.isDeleted = True
        request_object.save()
        serializer = RequestSerializer(request_object)
        return Response(serializer.data)


class RequestTest(APIView):
    "delete request"

    def get_object(self, request):
        try:
            request_obeject = Request.objects.get(
                requestId=request.data['requestId'])
            return request_obeject
        except Request.DoesNotExist:
            raise Http404

    def put(self, request, format=None):
        request_object = self.get_object(request)
        request_object.isDeleted = True
        request_object.save()
        serializer = RequestSerializer(request_object)
        return Response(serializer.data)
