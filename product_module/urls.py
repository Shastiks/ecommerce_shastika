from django.urls import path
from .views import index, index1
from .views import index,cart, removecart

urlpatterns = [
    path('', index),
    path('index1', index1),
]

urlpatterns = [
 path('', index),
 path('cart/', cart),
 path('cart/remove/<int:id>', removecart),
]