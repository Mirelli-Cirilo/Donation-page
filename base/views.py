from django.shortcuts import render, redirect
from django.conf import settings
import stripe

def product_page(request):
	
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
