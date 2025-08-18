from django.test import TestCase, SimpleTestCase
from django.core.exceptions import ValidationError
from second.models import Products


# net ninja way(pure python):
class TestProductModel(TestCase):
    def setUp(self):
        self.product = Products(name="pro1", price=100)

    def test_negative_price_validation(self):
        self.product.price = -10
        with self.assertRaises(ValidationError):
            self.product.clean()

    def test_in_stock_property(self):
        self.product.stock_count = 20
        self.assertTrue(self.product.in_stock)

        self.product.stock_count = 0
        self.assertFalse(self.product.in_stock)

    def test_get_discount_price(self):
        self.assertEqual(self.product.get_discount_price(10), 90)
        self.assertEqual(self.product.get_discount_price(50), 50)
        self.assertEqual(self.product.get_discount_price(0), 100)


# my way(using temp db):
class TestProductModelNima(TestCase):
    def setUp(self):
        self.product = Products.objects.create(name="pro1", price=100)

    def test_nima_negative_price_validation(self):
        self.product.price = -10
        with self.assertRaises(ValidationError):
            self.product.full_clean()
            self.product.save()

    def test_nima_in_stock_property(self):
        self.product.stock_count = 20
        self.product.save()
        self.assertTrue(self.product.in_stock)

        self.product.stock_count = 0
        self.product.save()
        self.assertFalse(self.product.in_stock)

    def test_nima_get_discount_price(self):
        self.assertEqual(self.product.get_discount_price(10), 90)
        self.assertEqual(self.product.get_discount_price(50), 50)
        self.assertEqual(self.product.get_discount_price(0), 100)


class TestNimaHintSimple(SimpleTestCase):
    # simple test case for the tests that does not need any DB operations or any PKs
    pass


class TestNimaHintSetUpTestData(TestCase):
    # setUpTestData just runs onece before all methods and it's more fast(good for heavy db operations)

    @classmethod
    def setUpTestData(cls):
        cls.product = Products.objects.create(name="pro1", price=100)
        # make sure you use cls.product in other methods in order to access the data
