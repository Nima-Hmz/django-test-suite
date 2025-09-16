from django.test import SimpleTestCase, TestCase
from model_test.models import Products
from django.urls import reverse

class TestIndexView(SimpleTestCase):
    def test_index_page_status_code(self):
        response = self.client.get('/')
        self.assertEqual(response.status_code, 200)

    def test_index_page_uses_correct_template(self):
        response = self.client.get('/')
        self.assertTemplateUsed(response, 'third/index.html')

    def test_index_page_contains_my_message(self):
        response = self.client.get('/')
        self.assertContains(response, 'my')


class TestProductsView(TestCase):
    
    @classmethod
    def setUpTestData(cls):
        cls.pro1 = Products.objects.create(name="pro1", price=200)
        cls.pro2 = Products.objects.create(name="pro2", price=300)

    def test_correct_template(self):
        response = self.client.get(reverse('third:products'))
        self.assertTemplateUsed('third/products.html')

    def test_products_context(self):
        response = self.client.get(reverse('third:products'))
        
        self.assertEqual(len(response.context['products']), 2)
        self.assertContains(response, 'pro1')
        self.assertNotContains(response, 'no product available')


    def test_no_product_available_message(self):
        self.__class__.pro1.delete()
        self.__class__.pro2.delete()

        response = self.client.get(reverse('third:products'))
        self.assertContains(response, 'no product available')

