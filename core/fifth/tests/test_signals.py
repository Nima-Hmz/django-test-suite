from django.test import TestCase
from unittest.mock import Mock, patch
from second.models import Products

class TestSignal(TestCase):
    def test_signal_products_save(self):
        with patch('fifth.signals.send_email', autospec=True) as mock_get:
            
            # creating the product
            Products.objects.create(name="terst", price=222, stock_count=3)

            # check if the signal was fired 
            mock_get.assert_called_once()
        

    def test_no_signal_products_update(self):

        with patch('fifth.signals.send_email', autospec=True) as mock_get:
            
            pro1 = Products.objects.create(name="terst", price=222, stock_count=3)

            mock_get.reset_mock()

            pro1.name = 'test2'
            pro1.save()

            mock_get.assert_not_called()
            

