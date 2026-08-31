import uuid
from django.test import SimpleTestCase
from django.urls import reverse, resolve, NoReverseMatch

from apps.accounts.urls import *
from apps.billing.urls import *
from apps.businesses.urls import *
from apps.rewards.urls import *


# docker compose exec backend python manage.py test tests.test_urls

"""
## Goal: Ensure the API endpoints resolve correctly and point to the expected views.
"""


class TestURLs(SimpleTestCase):

    def test_01_account_user_sign_up(self):
        """ Expected to pass """
        # Takes in the URL name from urls.py, returns path
        # Use when making a request to an endpoint
        url = reverse('account_signup')

        # Takes in URL path, returns information about the matched URL
        # Use when checking a URL points to the correct view
        resolved_url = resolve(url)

        # print(url)
        # print(resolved_url)
        # print(resolved_url.route)
        
        # .func.view_class returns the View defined in urls.py
        # print(resolved_url.func.view_class)
        
        self.assertEqual(resolved_url.url_name, 'account_signup')
        self.assertEqual(resolved_url.route, 'api/v1/accounts/signup/')
        self.assertTrue(resolved_url.func.view_class is AccountUserSignup)


    def test_02_business_register(self):
        """ Expected to pass """
        # Takes in the URL name from urls.py, returns path
        # Use when making a request to an endpoint
        url = reverse('business_register')

        # Takes in URL path, returns information about the matched URL
        # Use when checking a URL points to the correct view
        resolved_url = resolve(url)

        # print(url)
        # print(resolved_url)
        # print(resolved_url.route)
        
        # .func.view_class returns the View defined in urls.py
        # print(resolved_url.func.view_class)

        self.assertEqual(resolved_url.url_name, 'business_register')
        self.assertEqual(resolved_url.route, 'api/v1/businesses/register/')
        self.assertTrue(resolved_url.func.view_class is BusinessRegister)
        
        
    def test_03_business_location_with_two_uuids(self):
        """ Expected to pass """
        # Create UUIDs to pass into the URL
        business_id = uuid.uuid4()
        location_id = uuid.uuid4()

        # Pass both UUIDs into the path parameters
        url = reverse(
            'business_location_detail',
            kwargs = {'business_id': business_id, 'location_id': location_id})

        # Resolve the URL and check the passed UUIDs
        resolved_url = resolve(url)

        # print(url)
        # print(resolved_url)
        # print(resolved_url.route)
        # print(resolved_url.kwargs)
        
        # .func.view_class returns the View defined in urls.py
        # print(resolved_url.func.view_class)
        
        self.assertEqual(resolved_url.url_name, 'business_location_detail')
        self.assertEqual(resolved_url.route, 'api/v1/businesses/<uuid:business_id>/locations/<uuid:location_id>/')
        self.assertEqual(resolved_url.kwargs['business_id'], business_id)
        self.assertEqual(resolved_url.kwargs['location_id'], location_id)
        self.assertTrue(resolved_url.func.view_class is BusinessLocationDetail)


    def test_04_reward_with_uuid(self):
        """ Expected to pass """
        # Create a UUID to pass into the URL
        business_id = uuid.uuid4()
        
        # Takes in the URL name from urls.py, returns path
        # Leverage kwargs to test path parameters
        # Use when making a request to an endpoint
        url = reverse('rewards', kwargs = {'business_id': business_id})

        # Takes in URL path, returns information about the matched URL
        # Use when checking a URL points to the correct view
        resolved_url = resolve(url)

        # print(url)
        # print(resolved_url)
        # print(resolved_url.route)
        # print(resolved_url.kwargs)
        
        # .func.view_class returns the View defined in urls.py
        # print(resolved_url.func.view_class)

        self.assertEqual(resolved_url.url_name, 'rewards')
        self.assertEqual(resolved_url.route, 'api/v1/rewards/<uuid:business_id>/rewards/')
        self.assertEqual(resolved_url.kwargs['business_id'], business_id)
        self.assertTrue(resolved_url.func.view_class is RewardList)


    def test_05_billing_subscription(self):
        """ Expected to fail """
        # Takes in the URL name from urls.py, returns path
        # Leverage kwargs to test path parameters
        # business_id expects a UUID, passing an integer should fail
        with self.assertRaises(NoReverseMatch):
            reverse('billing_subscription', kwargs = {'business_id': 4})