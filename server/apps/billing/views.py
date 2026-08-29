from rest_framework.views import APIView
from rest_framework.response import Response
from djstripe.models import (
    Price,
    Product,
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