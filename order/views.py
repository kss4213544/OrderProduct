from django.shortcuts import render, redirect

from order.models import Order

def list_orders(request):
    orders = Order.objects.all()
    return render(request, 'order/list_orders.html.', {'orders': orders})


from order.forms import OrderForm

def create_order(request):
    form = OrderForm(request.POST or None)

    if form.is_valid():
        form.save()
        return redirect('list_orders')
    return render(request, 'order/order_form.html', {'form': form})

def update_order(request, order_id):
    order = Order.objects.get(order_id=order_id)
    form = OrderForm(request.POST or None, instance=order)

    if form.is_valid():
        form.save()
        return redirect('list_orders')

    return render(request, 'order/order_form.html', {'form': form, 'order': order})

def delete_order(request, order_id):
    order = Order.objects.get(order_id=order_id)

    if request.method == 'POST':
        order.delete()
        return redirect('list_orders')

    return render(request, 'order/order_delete_confirm.html', {'order': order})