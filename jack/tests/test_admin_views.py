from logging import getLogger

from django.conf import settings
from django.contrib.auth.models import User
from django.test import TestCase
from django.urls import reverse

# superuser
SU = 'su'
ST = 'staff'
NB = 'nobody'
PW = 'password'

log = getLogger(settings.DEBUG_LOGGER)


class AdminViewsTests(TestCase):
    # set up and tear down
    def setUp(self):
        # create a normal user
        self.nb = User.objects.create_user(
            username=NB, password=PW, is_staff=False, is_superuser=False
        )
        # create a staff user with no permissions
        self.st = User.objects.create_user(
            username=ST, password=PW, is_staff=True, is_superuser=False
        )
        # create a superuser
        self.su = User.objects.create_user(
            username=SU, password=PW, is_staff=True, is_superuser=True
        )

    def tearDown(self):
        self.su.delete()
        self.nb.delete()

    # admin access tests
    def test_admin_index(self):
        url = reverse('admin:index')
        response = self.client.get(url)
        # should redirect to login
        self.assertEquals(response.status_code, 302)

        self.client.force_login(self.nb)
        response = self.client.get(url)
        # normal user should also fail and redirect to login
        self.assertEquals(response.status_code, 302)

        self.client.force_login(self.st)
        response = self.client.get(url)
        # staff user can login
        self.assertEquals(response.status_code, 200)

        url = reverse('admin:auth_user_changelist')
        response = self.client.get(url)
        # staff user with no permissions should be forbidden
        self.assertEquals(response.status_code, 403)

        self.client.force_login(self.su)
        response = self.client.get(url)
        # superuser should be okay
        self.assertEquals(response.status_code, 200)
