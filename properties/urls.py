from django.urls import path
from . import views
# from django.conf import settings
# from django.conf.urls.static import static


urlpatterns = [
    path('', views.PropertyView.as_view(), name='properties'),
    path('reserve/<int:apartment>', views.reserve_apartment, name='reserve-apartment'), 
    path('verify_transaction', views.payment, name='payment'),
    path('cron/incomplete-reservations', views.incomplete_reservations, name='incomplete-reservations'),
    path('<slug:slug>/', views.single_property, name='single-property'),
    path('<slug:slug>/<int:room_type>/', views.available_apartments, name='available-apartments')
    
        

] 

# if settings.DEBUG: # new
#     urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
