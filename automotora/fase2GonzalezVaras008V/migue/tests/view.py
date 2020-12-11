from django.test import TestCase UserRegisterView
from django.urls import reverse

class TestViews (TestCase):
    def test_UserRegisterView(self):
        usuario=ClienteModelTest()

        response = ClienteModelTest.get(reserve('list'))

        self.assertEquals(response.status_code,200)
        self.assertTemplateUsed(response, 'budget/Login.html')
