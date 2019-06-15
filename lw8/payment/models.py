import datetime
from django.db import models


class Payment(models.Model):
    paymentSumm = models.IntegerField()
    userLogin = models.TextField()
    userEmail = models.EmailField()
    inputTime = models.DateTimeField(auto_now_add=True)
    confirmed = models.BooleanField()
    description = models.TextField()

    def __str__(self):
        return self.description

class ReturnPayment(models.Model):
    payment_id = models.ForeignKey('Payment', related_name='payments', on_delete=models.CASCADE)
    #paymentDescription = models.ForeignKey()