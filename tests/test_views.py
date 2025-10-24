from django.contrib.auth.models import User
from django.test import TestCase
from restaurant.models import Menu
from restaurant.serializers import MenuSerializer
from rest_framework.test import APIClient
from rest_framework import status
from rest_framework.authtoken.models import Token  # make sure to import this

class MenuViewTest(TestCase):
    def setUp(self):
        # Create a test user
        self.user = User.objects.create_user(username='testuser', password='employee@123!')
        self.client = APIClient()

        # Create token and attach to client
        token = Token.objects.create(user=self.user)
        self.client.credentials(HTTP_AUTHORIZATION=f'Token {token.key}')

        # Add some Menu objects for testing
        self.item1 = Menu.objects.create(name="IceCream", price=80, description="sweet & cold")
        self.item2 = Menu.objects.create(name="Burger", price=120, description="tasty & filling")
        self.item3 = Menu.objects.create(name="Pizza", price=150, description="cheesy & yummy")

    def test_getall(self):
        # Get all Menu items via API
        response = self.client.get("/restaurant/menu/")

        # Get data directly from DB and serialize
        items = Menu.objects.all()
        serializer = MenuSerializer(items, many=True)

        # Check that response matches serialized data
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data, serializer.data)
