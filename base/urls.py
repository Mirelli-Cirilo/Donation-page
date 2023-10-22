from django.urls import path
from . import views

urlpatterns = [
    path('', views.product_page, name='home'),
	path('payment_successful', views.payment_successful, name='payment_successful'),
	path('payment_cancelled', views.payment_cancelled, name='payment_cancelled')
	
]