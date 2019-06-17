from django.contrib import admin

from .models import Payment, ReturnPayment

admin.site.register(Payment)
admin.site.register(ReturnPayment)
