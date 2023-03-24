from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='home'),
    path('index/', views.index, name='main'),
    path('contact/', views.contact, name='contact'),
    path('product/', views.product, name='product'),
    path('about/', views.about, name='about'),

]
