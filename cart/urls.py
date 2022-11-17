from django.urls import path,include
from . import views
urlpatterns = [
    path('list/',views.cart,name='cart'),
    path('add/<int:pk>',views.cart_add,name='cart_add'),
    path('remove/<int:pk>/',views.cart_remove,name='cart_remove'),
    path('qty/update/',views.quantity_update,name='qty_update')
]
