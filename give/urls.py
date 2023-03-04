from django.urls import path
from . import views

urlpatterns = [

    # Stripe Payment Intent
    path('create-payment-intent/', views.CreateCheckoutSessionView, name='donations-checkout-session'),
    
    # Giving Pages
    path('', views.DonationsHome, name='donations-home'),
    path('success', views.Success, name='donations-success'),
    path('failure', views.Failure, name='donations-failure'),
]