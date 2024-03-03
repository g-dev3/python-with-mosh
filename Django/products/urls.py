from django.urls import path
from . import views

# /products
# /products/1/new

urlpatterns = [
    path('',views.index),
    path('new',views.new),
    path('new/byme',views.byme),
    path('new/byme/gdev',views.gdev)
]