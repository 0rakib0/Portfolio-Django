from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('view-project/<id>/', views.ViewPorfolio, name='view_protfolio')
]
