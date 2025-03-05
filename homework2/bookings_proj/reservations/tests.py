from django.test import TestCase
from .models import Movie, Seat, Booking
from django.utils import timezone

class MovieModelTest(TestCase):
    def test_str(self):
        movie = Movie.objects.create(title="Title", description="desc", release_date=timezone.now(), duration=90)
        self.assertEqual(str(movie), "Title")

class SeatModelTest(TestCase):
    def setUp(self):
        self.movie = Movie.objects.create(title="Title", description="desc", release_date=timezone.now(), duration=90)
        Seat.objects.filter(movie=self.movie).delete()

    def test_str(self):
        seat = Seat.objects.create(movie=self.movie, seat_number=5, is_booked=False)
        self.assertEqual(str(seat), "Seat 5 - Available")
        seat = Seat.objects.create(movie=self.movie, seat_number=2, is_booked=True)
        self.assertEqual(str(seat), "Seat 2 - Booked")

    def test_seat_status(self):
        seat = Seat.objects.create(movie=self.movie, seat_number=6, is_booked=False)
        self.assertEqual(seat.is_booked, False)
        seat.is_booked = True
        seat.save()
        self.assertEqual(seat.is_booked, True)

class BookingModelTest(TestCase):       
    def setUp(self):
        self.movie = Movie.objects.create(title="Title", description="desc", release_date=timezone.now(), duration=90)

    def test_booking_creation(self):
        seat = Seat.objects.get(seat_number=1)
        booking = Booking.objects.create(movie=self.movie, seat=seat)
        self.assertEqual(booking.movie.title, "Title")
        self.assertEqual(booking.seat, seat)
        self.assertEqual(booking.movie, self.movie)
    
    def test_booking_for_booked_seat(self):
        seat = Seat.objects.get(seat_number=1)
        Booking.objects.create(seat=seat, movie=self.movie)
        with self.assertRaises(Exception):
            Booking.objects.create(seat=seat, movie=self.movie)