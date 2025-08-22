from django.urls import path
from Store import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('', views.index, name='index'),
    path('register/', views.register, name='register'),
    path('products/', views.products, name='products'),

   
]



