from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status

from .models import Payment
from .serializers import PaymentSerializer


@api_view(['GET', 'DELETE', 'PUT'])
def get_delete_update_payments(request, pk):
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
    elif request.method == 'DELETE':
        return Response({})    

@api_view(['GET', 'POST'])
def get_post_payments(request):

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
            'confirm': request.data.get('confirm')
        }
        serializer = PaymentSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)