from django.shortcuts import render, get_object_or_404

from .models import Order


def orders(request):
    orders_list = Order.objects.all()
    context = {'orders_list': orders_list}
    return render(request, 'orders/orders.html', context)


def order(request, order_id):
    my_order = get_object_or_404(Order, id=order_id)
    context = {'order': my_order}
    return render(request, 'orders/order.html', context)
