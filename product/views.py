from django.shortcuts import render, redirect

from product.models import Product

def list_products(request):
    products = Product.objects.all()
    return render(request, 'product/list_products.html.', {'products': products})


from product.forms import ProductForm

def create_product(request):
    form = ProductForm(request.POST or None)

    if form.is_valid():
        form.save()
        return redirect('list_products')
    return render(request, 'product/product_form.html', {'form': form})

def update_product(request, product_id):
    product = Product.objects.get(product_id=product_id)
    form = ProductForm(request.POST or None, instance=product)

    if form.is_valid():
        form.save()
        return redirect('list_products')

    return render(request, 'product/product_form.html', {'form': form, 'product': product})

def delete_product(request, product_id):
    product = Product.objects.get(product_id=product_id)

    if request.method == 'POST':
        product.delete()
        return redirect('list_products')

    return
