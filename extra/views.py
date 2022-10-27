
# class UsersDetail(APIView):
#     "Retrieve, update or delete a user instance."

#     def get_object(self, pk):
#         try:
#             return Users.objects.get(memberId=pk)
#         except Users.DoesNotExist:
#             raise Http404

#     def get(self, request, pk, format=None):
#         users = self.get_object(pk)
#         serializer = UserSerializer(users)
#         return Response(serializer.data)

#     def put(self, request, pk, format=None):
#         users = self.get_object(pk)
#         serializer = UserSerializer(users, data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data)
#         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

#     def delete(self, request, pk, format=None):
#         users = self.get_object(pk)
#         users.delete()
#         return Response(status=status.HTTP_204_NO_CONTENT)
