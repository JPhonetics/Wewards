import uuid
from django.test import TestCase
from django.urls import reverse
from rest_framework import status

from apps.accounts.models import AccountUser
from apps.accounts.views import tokens_for
from apps.rewards.models import RewardProgramType


# docker compose exec backend python manage.py test tests.test_views

"""
## Goal: Ensure the API endpoints handle requests and return the expected responses.
"""


class TestViews(TestCase):

    def setUp(self):
        # Create test data that will be used across multiple tests
        self.user = AccountUser.objects.create_user(
            country = 'US',
            first_name = 'Vash',
            last_name = 'The Stampede',
            email = 'vash@anime.com',
            phone_number = '0000000000',
            password = '1234qwer',
        )
    
    
    def authenticate_test_user(
        self,
        client,
        user,
    ):
        # Create JWT tokens for the test user
        access, refresh = tokens_for(
            user
        )

        # Add the tokens to the test client's cookies
        client.cookies['access'] = access
        client.cookies['refresh'] = refresh

        return client


    def test_01_account_login_missing_username(self):
        """ Expected to fail """

        # Attempt to login without an email or phone number using post request
        # Send the data as json
        url = reverse('account_login')
        
        response = self.client.post(
            url,
            {
                'password': '1234qwer',
            },
            content_type = 'application/json'
        )
        
        # print(url)
        # print(response.status_code)
        # print(response.content)
        # print(response.json())

        # Ensure missing login information returns a bad request
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
        self.assertEqual(response.json(), 'Email or phone number is required.')


    def test_02_account_signup_invalid_data(self):
        """ Expected to fail """

        # Attempt to create an account with invalid data using post request
        # Send the data as json
        url = reverse('account_signup')

        response = self.client.post(
            url,
            {
                'country': 'US1',
                'first_name': 'Vash@',
                'last_name': 'Stampede^',
                'email': 'vash@anime',
                'phone_number': '000000!0000',
                'password': '1234qwer',
            },
            content_type = 'application/json'
        )
        
        # print(url)
        # print(response.status_code)
        # print(response.content)
        # print(response.json())

        # Ensure invalid account data returns a bad request
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)

        # Ensure the invalid fields returned validation errors
        self.assertIn('country', response.json())
        self.assertIn('email', response.json())
        self.assertIn('phone_number', response.json())


    def test_03_business_not_found(self):
        """ Expected to fail """

        # Create a UUID for a business the user does not belong to
        business_id = uuid.uuid4()

        # Authenticate the test user
        self.authenticate_test_user(self.client, self.user)

        # Attempt to access a business the user does not belong to
        response = self.client.get(
            reverse(
                'business_detail',
                kwargs = {
                    'business_id': business_id
                }
            )
        )
        
        # print(response.status_code)
        # print(response.json())

        # Ensure the business cannot be accessed
        self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)

        self.assertEqual(
            response.json(),
            {
                'detail': 'Business not found.'
            }
        )


    def test_04_reward_program_types(self):
        """ Expected to pass """

        # Create entries for the view to return
        RewardProgramType.objects.create(
            name = 'Points',
            description = 'Earn points for purchases.',
        )

        RewardProgramType.objects.create(
            name = 'Punch Card',
            description = 'Reward repeat purchases.',
        )

        # Authenticate the test user
        self.authenticate_test_user(self.client, self.user)

        # Client sends a GET request to a URL path by URL name
        url = reverse('reward_program_types')
        response = self.client.get(url)

        # Convert the JSON response into Python data
        response_body = response.json()

        # print(url)
        # print(response.status_code)
        # print(response.content)
        # print(response_body)
        # print(RewardProgramType.objects.count())

        # Ensure the request was successful
        self.assertEqual(response.status_code, status.HTTP_200_OK)

        # Ensure both entries were returned
        self.assertEqual(len(response_body), 2)

        # Ensure the returned entries contain the expected data
        self.assertEqual(response_body[0]['name'], 'Points')
        self.assertEqual(response_body[0]['description'], 'Earn points for purchases.')
        self.assertEqual(response_body[1]['name'], 'Punch Card')
        self.assertEqual(response_body[1]['description'], 'Reward repeat purchases.')


    def test_05_billing_products_empty(self):
        """ Expected to pass """

        # Client sends a GET request to a URL path by URL name
        # Expecting the database table to be empty
        url = reverse('billing_products')

        response = self.client.get(url)

        # Convert the JSON response into Python data
        response_body = response.json()

        # print(url)
        # print(response.status_code)
        # print(response.content)
        # print(response_body)

        # Ensure the request was successful
        self.assertEqual(response.status_code, status.HTTP_200_OK)

        # Ensure an empty product list is returned
        self.assertEqual(
            response_body,
            {
                'products': []
            }
        )