from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from rest_framework.urlpatterns import format_suffix_patterns
from django.urls import path
from . import views
app_name = "endpoints"


urlpatterns = [
    path('user/', views.CreateUser.as_view()),
    path('users/', views.UsersList.as_view()),
    path('user/<str:userId>/', views.UsersById.as_view()),
    path('user/update/<str:userId>/', views.UpdateUser.as_view()),
    path('user/updatePin/<str:userId>/', views.UpdatePin.as_view()),
    path('user/updateEmail/<str:userId>/', views.UpdateEmail.as_view()),
    path('documents/update/<str:userId>/', views.UpdateUserDocuments.as_view()),
    path('user/updatePhone/<str:userId>/',
         views.UpdateUserPhoneNumber.as_view()),
    path('user/delete/<str:userId>/', views.DeleteUser.as_view()),
    path('user/recover/<str:userId>/', views.RecoverUser.as_view()),
    path('requests/', views.RequestList.as_view()),
    path('requests/create/', views.RequestList.as_view()),
    path('request/<str:requestId>/', views.RequestById.as_view()),
    path('updateRequest/', views.UpdateRequest.as_view()),
    path('deleteRequest/', views.DeleteRequest.as_view()),



]

urlpatterns += format_suffix_patterns(urlpatterns)
