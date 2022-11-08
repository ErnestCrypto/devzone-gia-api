from django.test import TestCase, SimpleTestCase
from django.urls import reverse, resolve
from endpoints import views
# Create your tests for endpoints here.


class ApiUrlsTests(SimpleTestCase):

    def test_get_users_is_resolved(self):
        url = reverse('endpoints:getUsers')
        self.assertEquals(resolve(url).func.view_class, views.UsersList)

    def test_get_users_by_id_is_resolved(self):
        url = reverse('endpoints:getUsersById', args=('userId',))
        self.assertEquals(resolve(url).func.view_class, views.UsersById)

    def test_update_user_by_id_is_resolved(self):
        url = reverse('endpoints:updateUsers', args=('userId',))
        self.assertEquals(resolve(url).func.view_class, views.UpdateUser)

    def test_update_pin_is_resolved(self):
        url = reverse('endpoints:updatePin', args=('userId',))
        self.assertEquals(resolve(url).func.view_class, views.UpdatePin)

    def test_update_email_is_resolved(self):
        url = reverse('endpoints:updateEmail', args=('userId',))
        self.assertEquals(resolve(url).func.view_class, views.UpdateEmail)

    def test_update_address_is_resolved(self):
        url = reverse('endpoints:updateAddress', args=('userId',))
        self.assertEquals(resolve(url).func.view_class,
                          views.UpdateUserAddress)

    def test_update_documents_is_resolved(self):
        url = reverse('endpoints:updateDocuments', args=('userId',))
        self.assertEquals(resolve(url).func.view_class,
                          views.UpdateUserDocuments)

    def test_update_phone_is_resolved(self):
        url = reverse('endpoints:updatePhone', args=('userId', 'phoneId',))
        self.assertEquals(resolve(url).func.view_class,
                          views.UpdateUserPhoneNumber)

    def test_delete_user_is_resolved(self):
        url = reverse('endpoints:deleteUser', args=('userId', ))
        self.assertEquals(resolve(url).func.view_class,
                          views.DeleteUser)

    def test_recover_user_is_resolved(self):
        url = reverse('endpoints:recoverUser', args=('userId', ))
        self.assertEquals(resolve(url).func.view_class,
                          views.RecoverUser)

    def test_get_requests_is_resolved(self):
        url = reverse('endpoints:requests')
        self.assertEquals(resolve(url).func.view_class,
                          views.RequestList)

    def test_create_requests_is_resolved(self):
        url = reverse('endpoints:createRequest')
        self.assertEquals(resolve(url).func.view_class,
                          views.RequestList)

    def test_get_requests_by_id_is_resolved(self):
        url = reverse('endpoints:getRequestById', args=('resquestId',))
        self.assertEquals(resolve(url).func.view_class,
                          views.RequestById)

    def test_update_requests_by_id_is_resolved(self):
        url = reverse('endpoints:updateRequest', args=('resquestId',))
        self.assertEquals(resolve(url).func.view_class,
                          views.UpdateRequest)

    def test_delete_requests_by_id_is_resolved(self):
        url = reverse('endpoints:deleteRequest', args=('resquestId',))
        self.assertEquals(resolve(url).func.view_class,
                          views.DeleteRequest)

    def test_get_activities_is_resolved(self):
        url = reverse('endpoints:getUserActivitites', args=('userId',))
        self.assertEquals(resolve(url).func.view_class,
                          views.UserActivityById)
