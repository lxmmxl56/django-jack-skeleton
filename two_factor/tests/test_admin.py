from django.conf import settings
from django.shortcuts import resolve_url
from django.test import TestCase
from django.test.utils import override_settings

from two_factor.admin import patch_admin, unpatch_admin


class AdminPatchTest(TestCase):

    def setUp(self):
        patch_admin()

    def tearDown(self):
        unpatch_admin()

    def test(self):
        response = self.client.get('/admin/', follow=True)
        redirect_to = '%s?next=/en/admin/' % resolve_url(settings.LOGIN_URL)
        self.assertRedirects(response, redirect_to)

    @override_settings(LOGIN_URL='login')
    def test_named_url(self):
        response = self.client.get('/admin/', follow=True)
        redirect_to = '%s?next=/en/admin/' % resolve_url(settings.LOGIN_URL)
        self.assertRedirects(response, redirect_to)
