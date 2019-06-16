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

    # delete a single payment
    elif request.method == 'DELETE':
        return Response({})

    # update details of a single payment
    elif request.method == 'PUT':
        return Response({})

@api_view(['GET', 'POST'])
def get_post_payments(request):
    
    # get all payment
    if request.method == 'GET':
        payments = Payment.objects.all()
        serializer = PaymentSerializer(payments, many=True)
        return Response(serializer.data)

    # insert a new record for a payment
    elif request.method == 'POST':
        return Response({})