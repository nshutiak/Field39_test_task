from django.test import TestCase

import unittest
from django.test import TestCase
from .views import CreateFormView
from .models import Userdata


class CreateFormViewTestCase(TestCase):

    def setUp(self):
        self.view = CreateFormView()

    def test_model(self):
        self.assertEqual(self.view.model, Userdata)

    def test_fields(self):
        self.assertEqual(self.view.fields,
                        ('username', 'password', 'email', 'phone_number'))
