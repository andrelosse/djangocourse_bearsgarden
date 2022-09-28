from django.contrib import admin
from django.urls import path
from pizza import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.index, name='index'),
    path('order', views.order, name='order'),
    path('pizzas', views.pizzas, name='pizzas'),
]
