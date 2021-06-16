from django.urls import path

from order import views

urlpatterns = [
    path('', views.list_orders, name='list_orders'),
    path('new/', views.create_order, name='add_order'),
    path('update/<int:order_id>/', views.update_order, name='update_order'),
    path('delete/<int:order_id>/', views.delete_order, name='delete_order'),
    path('viewbar', views.viewbar, name = 'viewbar'),
]
