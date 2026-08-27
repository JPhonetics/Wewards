from django.test import TestCase
from django.core.exceptions import ValidationError
from apps.accounts.models import AccountUser


# docker compose exec backend python manage.py test tests.test_views


class UserTest(TestCase):
    
    def test_01_create_user(self):
        # Create user with good data
        new_user = AccountUser(
            country = 'US',
            first_name = 'Vash',
            last_name = 'The Stampede',
            email = 'vash@anime.com',
            phone_number = '0000000000',
            password = '1234qwer',
        )
        new_user.full_clean()
        
        self.assertIsNotNone(new_user)
        self.assertEqual(new_user.first_name, 'Vash')
        self.assertEqual(new_user.email, 'vash@anime.com')
            
            
    def test_02_create_user_using_manager(self):
        # Create user using custom manager
        new_user = AccountUser.objects.create_user(
            country = 'US',
            first_name = 'Vash',
            last_name = 'The Stampede',
            email = 'vash@anime.com',
            phone_number = '0000000000',
            password = '1234qwer',
        )
        new_user.full_clean()
        
        self.assertEqual(AccountUser.objects.count(), 1)
        self.assertEqual(new_user.country, 'US')
        
        
    def test_03_create_user_blank_entries(self):
        # Attempting to enter blank entries into required fields
        new_user = AccountUser(
            country = '',
            first_name = '',
            last_name = '',
            email = '',
            phone_number = '',
            password = '1234qwer',
        )
        with self.assertRaises(ValidationError) as context:
            new_user.full_clean()
            
        # print(context.exception.message_dict)
        
        self.assertTrue('This field cannot be blank.' in context.exception.message_dict['country'])
        self.assertTrue('This field cannot be blank.' in context.exception.message_dict['first_name'])
        self.assertTrue('This field cannot be blank.' in context.exception.message_dict['last_name'])
        self.assertTrue('This field cannot be blank.' in context.exception.message_dict['email'])
        self.assertTrue('This field cannot be blank.' in context.exception.message_dict['phone_number'])
        
        
    def test_03_create_user_test_validators(self):
        # Attempting to enter blank entries into required fields
        new_user = AccountUser(
            country = 'US1',
            first_name = 'Vash@',
            last_name = 'The Stampede^',
            email = 'vash@anime',
            phone_number = '000000!0000',
            password = '1234qwer',
        )
        with self.assertRaises(ValidationError) as context:
            new_user.full_clean()
            
        # print(context.exception.message_dict)
        
        self.assertTrue('Value \'US1\' is not a valid choice.' in context.exception.message_dict['country'])
        self.assertTrue('Please enter a valid first name.' in context.exception.message_dict['first_name'])
        self.assertTrue('Please enter a valid last name.' in context.exception.message_dict['last_name'])
        self.assertTrue('Enter a valid email address.' in context.exception.message_dict['email'])
        self.assertTrue('Please enter numbers only.' in context.exception.message_dict['phone_number'])
        
        
    def test_04_create_user_duplicate_unique_fields(self):
        AccountUser.objects.create_user(
            country = 'US',
            first_name = 'Vash',
            last_name = 'The Stampede',
            email = 'vash@anime.com',
            phone_number = '0000000000',
        )
        new_user = AccountUser(
            country = 'US',
            first_name = 'Ichigo',
            last_name = 'Kurosaki',
            email = 'vash@anime.com',
            phone_number = '0000000000',
            password = '1234qwer',
        )
        with self.assertRaises(ValidationError) as context:
            new_user.full_clean()

        # print(context.exception.message_dict)

        self.assertIn(
            'User with this Email already exists.',
            context.exception.message_dict['email']
        )
        self.assertIn(
            'User with this Phone Number already exists.',
            context.exception.message_dict['phone_number']
        )