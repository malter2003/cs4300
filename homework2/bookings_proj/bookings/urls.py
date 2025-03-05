from django.contrib import admin
from django.urls import path, include
from django.views.generic import RedirectView
from reservations import views as reservation_views

urlpatterns = [
    path('', RedirectView.as_view(url='/movies/', permanent=False)),
    path('admin/', admin.site.urls),
    path('movies/', reservation_views.movie_list, name='movie_list'),
    path('bookings/', reservation_views.booking_history, name='booking_history'),
    path('seats/<int:movie_id>/', reservation_views.seat_booking, name='seat_booking'),
    path('book-seat/<int:seat_id>/', reservation_views.book_seat, name='book_seat'),
    path('api/', include('reservations.urls')),
]