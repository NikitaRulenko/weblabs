from django.urls import path

from . import views


app_name = "payments"
# app_name will help us do a reverse look-up latter.

urlpatterns = [
    path('api/v1/payments/', views.getall_add_payments, name='getall_add_payments'),
    path('api/v1/payments/<int:pk>', views.getone_delete_update_payment, name='getone_delete_update_payment'),
    path('api/v1/payments/<int:pk>/confirm', views.confirm_payments, name='confirm_payments'),
    path('api/v1/payments/<int:pk>/cancel', views.cancel_payments, name='cancel_payments'),
]
