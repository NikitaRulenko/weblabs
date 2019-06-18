from django.contrib import admin

from .models import Payment, RefundPayment

admin.site.register(Payment)
admin.site.register(RefundPayment)
