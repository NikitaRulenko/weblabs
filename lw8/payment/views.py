from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
import datetime
from datetime import timedelta, timezone

from .models import Payment, RefundPayment
from .serializers import PaymentSerializer

@api_view(['GET'])
def refund_payment(request, pk):
    try:
        payment = Payment.objects.get(pk=pk)
        refund = RefundPayment.objects.create(payment_id=payment.id)
    except RefundPayment.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

@api_view(['GET', 'DELETE', 'PUT'])
def getone_delete_update_payment(request, pk):
    try:
        payment = Payment.objects.get(pk=pk)
    except Payment.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    # get details of a single payment
    if request.method == 'GET':
        serializer = PaymentSerializer(payment)
        return Response(serializer.data)

    # update details of a single payment
    if request.method == 'PUT':
        serializer = PaymentSerializer(payment, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_204_NO_CONTENT)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    # delete a single payment
    if request.method == 'DELETE':
        payment.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)  

#confirmation method
@api_view(['GET'])
def confirm_payments(request, pk):
    try: 
        payment = Payment.objects.get(pk=pk)
        payment.confirm = True
        payment.save()
    except Payment.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)   

    if request.method == 'GET':
        #data = {'confirm': request.data.get('confirm: true')}
        now = datetime.datetime.now(timezone.utc)
        then = payment.confirmTime

        if then > now:    
            payment.confirm = True
            payment.save()
            return Response('{Payment confirmed!}')
        else: 
            payment.confirm = False
            payment.save()
            return Response('{Cant create a payment: OVERTIME}')      

#cancel method
@api_view(['GET'])
def cancel_payments(request, pk): 
    try:
        payment = Payment.objects.get(pk=pk)
    except Payment.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        payment.cancel = True
        payment.save()
        return Response('{Payment canceled!}')        

@api_view(['GET', 'POST'])
def getall_add_payments(request):

    # get all payment
    if request.method == 'GET':
        payments = Payment.objects.all()
        serializer = PaymentSerializer(payments, many=True)
        return Response(serializer.data)

    # insert a new record for a payment
    if request.method == 'POST':
        data = {
            'userLogin': request.data.get('userLogin'),
            'userEmail': request.data.get('userEmail'),
            'paymentSumm': int(request.data.get('paymentSumm')),
            'description': request.data.get('description'),
            'confirm': request.data.get('confirm'),
            'cancel': request.data.get('cancel')
        }
        serializer = PaymentSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)