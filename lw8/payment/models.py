import datetime
from datetime import timedelta
from django.db import models


def get_delta():
    minute = timedelta(minutes=1)
    delta = datetime.datetime.now() + minute
    return delta

class Payment(models.Model):
    paymentSumm = models.IntegerField()
    userLogin = models.CharField(max_length=120)
    userEmail = models.EmailField()
    inputTime = models.DateTimeField(auto_now_add=True)
    confirm = models.BooleanField(default=True)
    description = models.TextField()
    confirmTime = models.DateTimeField(default=get_delta)
    cancel = models.BooleanField(default=True)

    def __str__(self):
        return self.description

class RefundPayment(models.Model):
    payment_id = models.ForeignKey('Payment', related_name='payments', on_delete=models.CASCADE)
    paymentDescription = models.TextField()
    approve = models.BooleanField()
    inputTime = models.DateTimeField(auto_now_add=True)
