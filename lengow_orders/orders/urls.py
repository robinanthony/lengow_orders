from . import views
from django.urls import path, include
from rest_framework import routers

router = routers.DefaultRouter()
router.register(r'order', views.OrderViewSet)

app_name = 'orders'
urlpatterns = [
    path('rest/', include(router.urls)),
    path('', views.orders, name='orders'),
    path('<str:order_id>', views.order, name='order'),
]
