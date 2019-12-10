from rest_framework import serializers
from .models import Order


class OrderSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Order
        fields = ('id', 'marketplace', 'idFlux', 'order_purchase_date', 'order_purchase_heure', 'order_amount',)
