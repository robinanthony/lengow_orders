from django.shortcuts import render, get_object_or_404
from .models import Order
from rest_framework import viewsets
from .serializers import OrderSerializer


def orders(request):
    context = dict()
    orders_list = Order.objects.all()

    if request.method == "POST":
        marketplace = request.POST.get('marketplace')
        idflux = request.POST.get('idflux')
        day = request.POST.get('day')
        month = request.POST.get('month')
        year = request.POST.get('year')

        if marketplace != '':
            orders_list = orders_list.filter(marketplace__icontains=marketplace)
            context['marketplace'] = marketplace
        if idflux != '':
            orders_list = orders_list.filter(idFlux=idflux)
            context['idflux'] = idflux
        if day != '':
            orders_list = orders_list.filter(order_purchase_date__day=day)
            context['day'] = day
        if month != '':
            orders_list = orders_list.filter(order_purchase_date__month=month)
            context['month'] = month
        if year != '':
            orders_list = orders_list.filter(order_purchase_date__year=year)
            context['year'] = year

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
