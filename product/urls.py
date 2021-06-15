from django.urls import path

from product import views

urlpatterns = [
    path('', views.list_products, name='list_products'),
    path('new/', views.create_product, name='add_product'),
    path('update/<int:product_id>/', views.update_product, name='update_product'),
    path('delete/<int:product_id>/', views.delete_product, name='delete_product'),
]
