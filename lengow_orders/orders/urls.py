from . import views
from django.urls import path


app_name = 'orders'
urlpatterns = [
    path('', views.orders, name='orders'),
    path('<str:order_id>', views.order, name='order'),
]
