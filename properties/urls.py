from django.urls import path
from . import views


urlpatterns = [
    path('', views.PropertyView.as_view(), name='properties'),
    path('reserve/<int:apartment>', views.reserve_apartment, name='reserve-apartment'), 
    path('<slug:slug>/', views.single_property, name='single-property'),
    path('<slug:slug>/<int:room_type>/', views.available_apartments, name='available-apartments')
        

]