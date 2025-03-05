from rest_framework import viewsets
from rest_framework.response import Response
from rest_framework.decorators import action
from .models import Movie, Seat, Booking
from .serializers import MovieSerializer, SeatSerializer, BookingSerializer
from django.shortcuts import render, get_object_or_404, redirect
from django.db.models.signals import post_save
from django.dispatch import receiver

class MovieViewSet(viewsets.ModelViewSet):
    queryset = Movie.objects.all()
    serializer_class = MovieSerializer

class SeatViewSet(viewsets.ModelViewSet):
    queryset = Seat.objects.all()
    serializer_class = SeatSerializer

    @action(detail=True, methods=['get'])
    def availability(self, request, pk=None):
        seat = self.get_object()
        return Response({"available": not seat.is_booked()})

    @action(detail=True, methods=['post'])
    def book_seat(self, request, pk=None):
        seat = self.get_object()
        if not seat.is_booked:
            seat.is_booked = True
            seat.save()
            Booking.objects.create(seat=seat, movie=seat.movie)
            return Response({"status": "Booked"})
        return Response({"status": "Already booked"}, status=400)

class BookingViewSet(viewsets.ModelViewSet):
    queryset = Booking.objects.all()
    serializer_class = BookingSerializer

    @action(detail=False, methods=['get'])
    def history(self, request):
        bookings = Booking.objects.all()
        serializer = self.get_serializer(bookings, many=True)
        return Response(serializer.data)

def movie_list(request):
    movies = Movie.objects.all()
    return render(request, 'reservations/movie_list.html', {'movies': movies})

def booking_history(request):
    bookings = Booking.objects.all()
    return render(request, 'reservations/booking_history.html', {'bookings': bookings})

def seat_booking(request, movie_id):
    movie = get_object_or_404(Movie, id=movie_id)
    seats = Seat.objects.filter(movie_id=movie_id)
    return render(request, 'reservations/seat_booking.html', {'movie': movie, 'seats': seats})

@receiver(post_save, sender=Movie)
def create_seats_for_movie(sender, instance, created, **kwargs):
    if created:
        for i in range(1, 21):
            Seat.objects.create(seat_number=f"{i}", is_booked=False, movie=instance)

def book_seat(request, seat_id):
    seat = get_object_or_404(Seat, id=seat_id)
    
    if not seat.is_booked:
        seat.is_booked = True
        seat.save()
        Booking.objects.create(seat=seat, movie=seat.movie)        
    return redirect('seat_booking', movie_id=seat.movie.id)