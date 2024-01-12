from django.urls import path , include
from . import views

urlpatterns = [
    path('', views.home , name = "home"),
    path('notes/', views.note , name = "notes"),
    path('delete/<int:pk>/' , views.delete , name  ="delete-note"),

]
