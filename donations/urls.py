from django.urls import path
from . import views

urlpatterns = [
    path('create-payment-intent/', views.CreateCheckoutSessionView, name='donations-checkout-session'),
    
    path('', views.DonationsHome.as_view(), name='donations-home'),
    path('success', views.Success, name='donations-success'),
    path('failure', views.Failure, name='donations-failure'),
]