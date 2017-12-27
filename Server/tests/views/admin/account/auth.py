import json
import unittest2 as unittest

from tests.views import admin

from server import app


class TestAuth(unittest.TestCase):
    def setUp(self):
        self.client = app.test_client()
        admin.create_fake_account()

    def tearDown(self):
        admin.remove_fake_account()

    def testA_auth(self):
        """
        TC about admin's auth

        1. Check 'login failed'
        2. Check 'login succeed'
        3. Check 'access token/refresh token'
        """
        rv = self.client.post('/admin/auth', data={'id': 'chicken', 'pw': 'chicken'})
        self.assertEqual(rv.status_code, 401)
        # Login fail : Incorrect ID or PW

        rv = self.client.post('/admin/auth', data={'id': 'fake', 'pw': 'fake'})
        self.assertEqual(rv.status_code, 200)
        # Success

        data = json.loads(rv.data.decode())
        self.assertTrue('access_token' in data and 'refresh_token' in data)
        # Token check

    def testB_refresh(self):
        """
        TC about admin's refresh

        1. Check 'unauthorized'
        2. Check 'refresh succeed'
        3. Check 'new access token'
        """
        rv = self.client.post('/admin/refresh')
        self.assertEqual(rv.status_code, 401)
        # Unauthorized check

        refresh_token = admin.get_refresh_token(self.client)
        rv = self.client.post('/admin/refresh', headers={'Authorization': refresh_token})
        self.assertEqual(rv.status_code, 200)
        # Success

        data = json.loads(rv.data.decode())
        self.assertTrue('access_token' in data)
        # New access token check