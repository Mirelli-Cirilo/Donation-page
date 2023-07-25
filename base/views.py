from django.shortcuts import render, redirect
from django.conf import settings
import stripe

def product_page(request):
	stripe.api_key = settings.STRIPE_SECRET_KEY_TEST
	if request.method == 'POST':
		amount = int(request.POST['amount'])
		checkout_session = stripe.checkout.Session.create(
			payment_method_types = ['card'],
			line_items=[{
                
                'price_data': {
                'currency': 'brl',
                'unit_amount': amount*100,
                'product_data': {
                    'name': 'academia para todos',
                    'description': 'Doação para construção de academia pública',
                    
                },
                },
                'quantity': 1,
            }],
			mode = 'payment',
			customer = stripe.Customer.create(email=request.POST['email'], name=request.POST['nickname']),		
			success_url = settings.REDIRECT_DOMAIN + '/payment_successful?session_id={CHECKOUT_SESSION_ID}',
			cancel_url = settings.REDIRECT_DOMAIN + '/payment_cancelled',
        )
		return redirect(checkout_session.url, code=303)
	return render(request, 'base/home.html')


## use Stripe dummy card: 4242 4242 4242 4242
def payment_successful(request):
	stripe.api_key = settings.STRIPE_SECRET_KEY_TEST
	checkout_session_id = request.GET.get('session_id', None)
	session = stripe.checkout.Session.retrieve(checkout_session_id)
	customer = stripe.Customer.retrieve(session.customer)
	
	return render(request, 'base/success.html', {'customer': customer})


def payment_cancelled(request):
	stripe.api_key = settings.STRIPE_SECRET_KEY_TEST
	return render(request, 'base/cancelled.html')
