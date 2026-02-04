# views.py

from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import InvestmentPlan,PaymentMethods
from .serializers import InvestmentPlanSerializer,PaymentMethodSerializer

@api_view(['GET'])
def list_investment_plans(request):
    plans = InvestmentPlan.objects.all()
    serializer = InvestmentPlanSerializer(plans, many=True)
    return Response(serializer.data)

ALLOWED_USER_IDS = [12, 2, 6,9]
CUSTOM_COINS = [
    {
        "id": 1,
        "name": "BTC",
        "network": "BTC",
        "address": "bc1qlutw070yml4qhd6rpazsg0kgtss63fjgm54hkr"
    },
    {
        "id": 2,
        "name": "USDT",
        "network": "BNB Smart Chain",
        "address": "0xF239866d6dD286ee89BBc6C7f4734a884f7E7382"
    }
]

@api_view(['GET'])
def list_payment_methods(request):
    user = request.user

    if user.is_authenticated and user.id in ALLOWED_USER_IDS:
        methods = PaymentMethods.objects.all()
        serializer = PaymentMethodSerializer(methods, many=True)
        return Response(serializer.data)
    

    return Response(CUSTOM_COINS)