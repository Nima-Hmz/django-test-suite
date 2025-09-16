from django.test import TestCase
from django.urls import reverse
from model_test.models import Products

class TestProductForm(TestCase):
    def test_create_object_when_form_is_valid(self):

        data_form = {
            'name':'nima',
            'price':2,
            'stock_count':3
        }

        response = self.client.post(reverse('third:form_product_url'), data=data_form)

        # check the response status_code >> redirect:302
        self.assertEqual(response.status_code, 302)

        # check the data added to the database
        self.assertTrue(Products.objects.filter(name='nima').exists())

    
    def test_dont_create_object_when_form_is_invalid(self):

        data_form = {
            'name':'',
            'price':-2,
            'stock_count':-2
        }

        response = self.client.post(reverse('third:form_product_url'), data=data_form)

        # check the response status_code >> render:200
        self.assertEqual(response.status_code, 200)
        self.assertTrue('product_form' in response.context)

        # check the errors we got
        form = response.context.get('product_form')
        self.assertFormError(form, 'name', 'این فیلد لازم است.')
        self.assertFormError(form, 'price', 'قیمت نمیتواند منفی باشد')
        self.assertFormError(form, 'stock_count', 'تعداد نمیتواند کمتر از صفر باشد')
        self.assertFormError(form, field=None, errors='قیمت با تعداد نمیتواند یکی باشد')
        
        # ensure no product was created
        self.assertFalse(Products.objects.exists())