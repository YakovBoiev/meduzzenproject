from django.contrib.auth.models import User
from rest_framework import status
from rest_framework.test import APITestCase, APIRequestFactory
from mixer.backend.django import mixer
from .models import User


class UserTestCase(APITestCase):

    def test_user(self):
        result = self.client.get('/user/')
        self.assertEqual(result.status_code, status.HTTP_200_OK)

    def test_read_user(self):
        admin = User.objects.create_superuser('admin', 'amin@admin.gmail.com', 'admin')
        response = self.client.get(f'/user/{admin.id}/')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data['username'], 'admin')
        self.assertEqual(response.data['email'], 'amin@admin.gmail.com')

    def test_post_user(self):
        self.user = mixer.blend(User)
        data = {'username': self.user.username, 'email': self.user.email, 'password': self.user.password}
        response = self.client.post('/user/', data)
        self.assertEqual(User.objects.count(), 1)

    # def test_update_user(self):
    #     admin = User.objects.create_superuser('admin', 'amin@admin.gmail.com', 'admin')
    #     self.user = mixer.blend(User)
    #     data = {'username': self.user.username, 'email': self.user.email, 'password': self.user.password}
    #     response = self.client.put(f'/user/{admin.id}/', data, format='json')
    #

    def test_delete_user(self):
        admin = User.objects.create_superuser('admin', 'amin@admin.gmail.com', 'admin')
        self.assertEqual(User.objects.count(), 1)
        response = self.client.delete(f'/user/{admin.id}/')
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
        self.assertEqual(User.objects.count(), 0)




