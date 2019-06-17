from django.urls import path

from . import views


app_name = "payments"
# app_name will help us do a reverse look-up latter.

urlpatterns = [
    path('api/v1/payments/', views.get_post_payments, name='get_post_payments'),
    path('api/v1/payments/<int:pk>', views.get_delete_update_payments, name='get_delete_update_payments'),
]
