# Imports
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# 3rd party:
from django.urls import path
# Internal
from . import views
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~


app_name = 'bookings'

urlpatterns = [
    path('', views.book, name='bookings'),
    path('mybookings/', views.mybookings, name='mybookings'),
    path('delete/<int:booking_id>/',
         views.delete_booking, name='delete_booking'),
    path('<int:booking_id>/change/',
         views.change_booking, name='change_booking'),
    path('confirmation/',
         views.booking_confirmation, name='booking_confirmation'),
]
