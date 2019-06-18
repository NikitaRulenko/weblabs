from rest_framework import serializers
from .models import Payment, RefundPayment


class PaymentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Payment
        fields = ('description', 'userLogin', 'userEmail', 'paymentSumm', 'inputTime', 'confirm', 'confirmTime', 'cancel')

class RefundSerializer(serializers.ModelSerializer):
    class Meta:
        model: RefundPayment
        fields = ('payment_id', 'paymentDescription')