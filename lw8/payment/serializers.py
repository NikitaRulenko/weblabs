from rest_framework import serializers
from .models import Payment


class PaymentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Payment
        fields = ('description', 'userLogin', 'userEmail', 'paymentSumm', 'inputTime', 'confirm', 'confirmTime', 'cancel')

