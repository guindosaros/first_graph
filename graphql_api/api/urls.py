
from django.urls import path
from .views import category, cat_ingredient ,ingredient

urlpatterns = [
    path('',category,name='category'),
    path('category/<str:pk>',cat_ingredient,name='ingredient_cat'),
    path('ingredient',ingredient,name='ingredient'),
]
