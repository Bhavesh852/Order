from django.urls import path
from . import views

urlpatterns = [
    path('', views.index),
    path('order_form/', views.order_form),
    path('list-page/', views.list_page),
    path('search/', views.SearchListView.as_view()),
    path('edit/<int:myid>/', views.edit),
    path('delete/<int:myid>/', views.delete_order),

]
