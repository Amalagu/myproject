from django.urls import path, include
from . import views
urlpatterns = [
    path('', views.indexpage, name='indexpage'),
    path('display/<int:id>/', views.displaypage, name='displaypage'),
    path('edit/<int:id>/', views.editpage, name='editpage'),
    path('commitchanges/<int:id>/', views.commitchanges, name='commitchanges'),
]
