from django.conf import settings
from rest_framework import status
from rest_framework.views import APIView
from rest_framework.response import Response

from djstripe.models import (
    Price,
    Product,
)
from core.lookups import (
    get_business,
    get_business_staff_for_user,
)
from apps.billing.services import (
    create_subscription_checkout,
    get_billing_customer,
    get_business_subscription_latest,
    get_billing_price,
    get_subscription_price,
)


class BillingProducts(APIView):
    
    def get(self, request):

        products = Product.objects.filter(active = True)
        
        # prices = Price.objects.filter(active = True)
        
        # # Use this to call the API and see what data returns
        # # Use it to format the actual response you want
        # prices = Price.objects.filter(active = True)
        # return Response(Prices.values())
    
        product_data = []
        
        for product in products:
            
            # As we loop through products find the matching prices objects            
            prices = Price.objects.filter(product = product, active = True)
            
            price_data = []
            
            # Loop through prices and create a dictionary
            # and put it inside price_data list
            for price in prices:
                
                price_data.append(
                    {
                        'id': price.id,
                        'name': price.metadata.get('nickname'),
                        'currency': price.currency,
                        'unit_amount': price.unit_amount,
                        'interval': price.recurring.get('interval'),
                    }
                )
            
            # As we are looping though product fill the dictionary 
            # embed price_data under prices to the matching product
            product_data.append(
                {
                    'id': product.id,
                    'name': product.name,
                    'description': product.description,
                    'prices': price_data,
                }
            )
        
        return Response(
            {
                'products': product_data
            }
        )
        
        
class BillingSubscription(APIView):
    
    def get(self, request, business_id):
        
        business = get_business(business_id)
        
        business_staff = get_business_staff_for_user(
            business_id,
            request.user.id,
        )
        
        subscription = get_business_subscription_latest(business)
        
        if not subscription:
            return Response(
                {
                    'product_name': None,
                    'status': None,
                    'trial_start': None,
                    'trial_end': None,
                    'start_date': None,
                    'ended_at': None,
                },
                status = status.HTTP_200_OK
            )
            
        price = get_subscription_price(subscription)
        
        return Response(
            {
                'product_id': price.product.id,
                'product_name': price.product.name,
                'price_id': price.id,
                'price_name': price.metadata.get('nickname'),
                'price_currency': price.currency,
                'price_unit_amount': price.unit_amount,
                'price_interval': price.recurring.get('interval'),
                'status': subscription.status,
                'trial_start': subscription.trial_start,
                'trial_end': subscription.trial_end,
                'start_date': subscription.start_date,
                'ended_at': subscription.ended_at,
            },
            status = status.HTTP_200_OK
        )
        
        
class BillingSubscribe(APIView):
    
    def post(self, request, business_id):
        
        # Get the business the user is subscribing for
        business = get_business(business_id)
        
        # Make sure the logged-in user belongs to this business
        business_staff = get_business_staff_for_user(
            business_id,
            request.user.id,
        )
        
        # Get the Stripe Price selected by the user
        price = get_billing_price(
            request.data.get('price_id')
        )
        
        # Get the business's current trial subscription
        subscription = get_business_subscription_latest(
            business
        )
        
        # Get the Stripe Customer linked to this business
        billing_customer = get_billing_customer(
            business
        )
        
        # Where Stripe sends the user after Checkout
        success_url = (
            f"{settings.CLIENT_URL}/business/{business.id}/billing"
            "?checkout=success"
        )
        
        cancel_url = (
            f"{settings.CLIENT_URL}/business/{business.id}/billing"
            "?checkout=cancel"
        )
        
        # Create the Stripe Checkout Session
        checkout = create_subscription_checkout(
            billing_customer,
            subscription,
            price,
            success_url,
            cancel_url,
        )
        
        # Send the Stripe Checkout URL back to React
        return Response(
            {
                'checkout_url': checkout.url
            },
            status = status.HTTP_200_OK
        )