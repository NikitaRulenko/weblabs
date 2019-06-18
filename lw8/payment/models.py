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
    confirm = models.BooleanField(blank=True)
    description = models.TextField()
    confirmTime = models.DateTimeField(default=get_delta)
    cancel = models.BooleanField(blank=True)

    def __str__(self):
        return self.description

    # def paymentTimeComfirm(self):
    #     minute = timedelta(minutes=1)
    #     if (inputTime + minute) > confirmTime:
    #         confirm = False

class RefundPayment(models.Model):
    payment_id = models.ForeignKey('Payment', related_name='payments', on_delete=models.CASCADE)
    paymentDescription = models.TextField()
    inputTime = models.DateTimeField(auto_now_add=True)