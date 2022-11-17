from django.urls import path,include
from . import views
urlpatterns = [
    path('list/',views.order,name='order'),
    path('details/<int:pk>',views.order_details,name='order_details')
]
