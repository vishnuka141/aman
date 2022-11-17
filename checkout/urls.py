from django.urls import path,include
from . import views
urlpatterns = [
    path('list/',views.check_out,name='check_out'),
    path('success/',views.success_page,name='success')
]
