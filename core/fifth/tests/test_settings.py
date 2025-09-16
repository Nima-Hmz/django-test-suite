from django.test import SimpleTestCase, override_settings, tag
from django.urls import reverse


@override_settings(MAINTAINANCE_MODE=False) # also you can set it on the class
class TestMaintainanceSettings(SimpleTestCase):

    @override_settings(MAINTAINANCE_MODE=True)
    def test_maintainance_on(self):
        response = self.client.get(reverse('third:index'))

        self.assertEqual(response.status_code, 503)


    @tag('off')
    @override_settings(MAINTAINANCE_MODE=False)
    def test_maintainance_off(self):
        response = self.client.get(reverse('third:index'))

        self.assertEqual(response.status_code, 200)


# you can also do it by creating a dedicated settins file just for the 
# test purpose.
# and then just run in like this:
# python manage.py test --settings=project.testsettings

# whta should be in the test settings ? 
# from project.settings import *
# custome_x = True