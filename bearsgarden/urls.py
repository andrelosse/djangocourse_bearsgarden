from django.contrib import admin
from django.urls import path, include
from bakery import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('accounts/', include('django.contrib.auth.urls')),
    path('register/', views.register, name='register'),
    path('history/', views.order_history, name='history'),
    path('', views.index, name='index'),
    path('order', views.order, name='order'),
    path('items', views.order_multiple, name='order_multiple'),
    path('order/<int:pk>', views.edit_order, name='edit_order')
]
