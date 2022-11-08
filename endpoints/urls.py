from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from rest_framework.urlpatterns import format_suffix_patterns
from django.urls import path
from . import views
app_name = "endpoints"


urlpatterns = [
    path('users/', views.UsersList.as_view(), name='getUsers'),
    path('users/<str:userId>/', views.UsersById.as_view(), name='getUsersById'),
    path('users/update/<str:userId>/',
         views.UpdateUser.as_view(), name='updateUsers'),
    path('users/updatePin/<str:userId>/',
         views.UpdatePin.as_view(), name='updatePin'),
    path('users/updateEmail/<str:userId>/',
         views.UpdateEmail.as_view(), name='updateEmail'),
    path('users/updateAddress/<str:userId>/',
         views.UpdateUserAddress.as_view(), name='updateAddress'),
    path('documents/update/<str:userId>/',
         views.UpdateUserDocuments.as_view(), name='updateDocuments'),
    path('users/updatePhone/<str:userId>/<str:phoneId>/',
         views.UpdateUserPhoneNumber.as_view(), name='updatePhone'),
    path('users/delete/<str:userId>/',
         views.DeleteUser.as_view(), name='deleteUser'),
    path('users/recover/<str:userId>/',
         views.RecoverUser.as_view(), name='recoverUser'),
    path('requests/', views.RequestList.as_view(), name='requests'),
    path('requests/create/', views.RequestList.as_view(), name='createRequest'),
    path('requests/<str:requestId>/',
         views.RequestById.as_view(), name='getRequestById'),
    path('requests/update/<str:requestId>/',
         views.UpdateRequest.as_view(), name='updateRequest'),
    path('requests/delete/<str:requestId>/',
         views.DeleteRequest.as_view(), name='deleteRequest'),
    path('activities/<str:userId>/',
         views.UserActivityById.as_view(), name='getUserActivitites'),




]

urlpatterns += format_suffix_patterns(urlpatterns)
