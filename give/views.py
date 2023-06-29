from django.shortcuts import render
import stripe
from django.views.decorators.csrf import csrf_exempt
from django.http import JsonResponse
from django.conf import settings
import json

stripe.api_key = str(settings.STRIPE_PRIVATE_KEY)

# Serves the stripe element on the giving homepage a client secret
@csrf_exempt
def CreateCheckoutSessionView(request,dollars):
    if request.method == "POST":
        intent = stripe.PaymentIntent.create(
            amount=int(dollars)*100,
            currency='usd',
            payment_method_types=['us_bank_account','card', 'cashapp','link'],
            payment_method_options={
                "us_bank_account": {
                    "financial_connections": {
                        "permissions": 
                            ["payment_method"]
                        }
                },
            },
        )

        return JsonResponse({
            'clientSecret': str(intent['client_secret'])
        })

# Redirect page in case of successful donation
def Success(request):
    context = {}
    return render(request, 'give/success.html', context)

# Redirect page in case of failed donation
def Failure(request):
    context = {}
    return render(request, 'give/failure.html', context)

# Donation Homepage
def DonationsHome(request):
    context = {
        'STRIPE_PUBLIC_KEY': settings.STRIPE_PUBLIC_KEY,
    }
    return render(request, 'give/index.html', context)




