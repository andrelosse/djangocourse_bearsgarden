from django.test import TestCase, Client
from django.contrib.auth.models import User
from .models import BakeryItem, Category

class BakeryTestCase(TestCase):
    def setUp(self):
        self.client = Client()
        self.user = User.objects.create_user(username='testuser', password='12345')
        self.category = Category.objects.create(name='Pastry')

    def test_order_view_requires_login(self):
        response = self.client.get('/order')
        self.assertEqual(response.status_code, 302)  # Redirect to login

    def test_order_view_post(self):
        self.client.login(username='testuser', password='12345')
        response = self.client.post('/order', {
            'name': 'Croissant',
            'description': 'Flaky pastry',
            'price': '3.50',
            'category': self.category.id
        })
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, 'Order completed!')
        self.assertTrue(BakeryItem.objects.filter(user=self.user).exists())