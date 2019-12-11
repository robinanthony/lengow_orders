from django.shortcuts import render, get_object_or_404
from .models import Order
from rest_framework import viewsets
from .serializers import OrderSerializer

# 'filter_name': 'field_name'
FIELD_SPECIFICATION = {
    'marketplace__icontains': 'marketplace',
    'idFlux': 'idflux',
    'order_purchase_date__day': 'day',
    'order_purchase_date__month': 'month',
    'order_purchase_date__year': 'year',
}


def orders(request):
    context = dict()
    orders_list = Order.objects.all()

    if request.method == "POST":
        for filter_name, field_name in FIELD_SPECIFICATION.items():
            field_value = request.POST.get(field_name)
            if field_value != '':
                print({filter_name: field_value})
                orders_list = orders_list.filter(**{filter_name: field_value})
                context[field_name] = field_value

    context['orders_list'] = orders_list
    return render(request, 'orders/orders.html', context)


def order(request, order_id):
    my_order = get_object_or_404(Order, id=order_id)
    context = {'order': my_order}
    return render(request, 'orders/order.html', context)


class OrderViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows orders to be viewed or edited.
    """
    queryset = Order.objects.all()
    serializer_class = OrderSerializer
