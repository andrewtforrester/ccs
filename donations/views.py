from django.shortcuts import render
import stripe
from django.views.generic.base import TemplateView
from django.views.decorators.csrf import csrf_exempt
from django.views import View
from django.utils.decorators import method_decorator
from django.http import JsonResponse, HttpResponse

import json
import os
import stripe

stripe.api_key = 'sk_test_51MhNQdKiI0BX1zB1T4eiZhXVjeUVu8scBLl8G6FbHBvtZXqpzX78vm78qN6PwVGhpzDhBO8V4ObdMmdtenhsn2N700cmzF8VZH'


# @method_decorator(csrf_exempt, name='dispatch')

@csrf_exempt
def CreateCheckoutSessionView(request):
    if request.method == "POST":
        intent = stripe.PaymentIntent.create(
            amount=1000,
            currency='usd',
            automatic_payment_methods={
                'enabled': True,
            },
        )

        return JsonResponse({
            'clientSecret': str(intent['client_secret'])
        })




def Success(request):
    context = {}
    return render(request, 'donations/success.html', context)

def Failure(request):
    context = {}
    return render(request, 'donations/failure.html', context)

class DonationsHome(TemplateView):
    template_name = 'donations/index.html'





