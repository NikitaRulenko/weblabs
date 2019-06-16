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
    confirm = models.BooleanField()
    description = models.TextField()
    confirmTime = models.DateTimeField(default=get_delta)

    def __str__(self):
        return self.description

    def paymentTimeComfirm(self):
        minute = timedelta(minutes=1)
        if (inputTime + minute) > confirmTime:
            confirm = False

class ReturnPayment(models.Model):
    payment_id = models.ForeignKey('Payment', related_name='payments', on_delete=models.CASCADE)
    #paymentDescription = models.ForeignKey()