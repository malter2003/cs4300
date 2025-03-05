from rest_framework import viewsets
from rest_framework.response import Response
from rest_framework.decorators import action
from .models import Movie, Seat, Booking
from .serializers import MovieSerializer, SeatSerializer, BookingSerializer
from django.shortcuts import render

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
    def book(self, request, pk=None):
        seat = self.get_object()
        if not seat.is_booked():
            seat.book()
            Booking.objects.create(user=request.user, seat=seat, movie=seat.movie)
            return Response({"status": "Booked"})
        return Response({"status": "Already booked"}, status=400)

class BookingViewSet(viewsets.ModelViewSet):
    queryset = Booking.objects.all()
    serializer_class = BookingSerializer

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)

    @action(detail=False, methods=['get'])
    def history(self, request):
        bookings = Booking.objects.filter(user=request.user)
        serializer = self.get_serializer(bookings, many=True)
        return Response(serializer.data)

def movie_list(request):
    movies = Movie.objects.all()
    return render(request, 'reservations/movie_list.html', {'movies': movies})

# View to render the booking list page
def booking_history(request):
    bookings = Booking.objects.filter(user=request.user)
    return render(request, 'reservations/booking_history.html', {'bookings': bookings})

# View to render the seat list page
def seat_booking(request):
    seats = Seat.objects.all()
    return render(request, 'reservations/seat_booking.html', {'seats': seats})