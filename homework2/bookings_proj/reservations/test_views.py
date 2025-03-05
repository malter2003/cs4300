from rest_framework.test import APITestCase
from rest_framework import status
from django.urls import reverse
from .models import Movie, Seat, Booking
from django.contrib.auth.models import User
from django.utils import timezone

class MovieViewSetTest(APITestCase):
    def setUp(self):
        self.movie = Movie.objects.create(title="Title", description="desc", release_date=timezone.now(), duration=90)

    def test_movie_list(self):
        response = self.client.get(reverse('movie-list'))
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data[0]['title'], "Title")

    def test_movie_create(self):
        response = self.client.get(reverse('movie-list'))
        data = {
            "title": "Some movie",
            "description": "some desc",
            "release_date": "2025-03-19",
            "duration": 120
        }
        response = self.client.post(reverse('movie-list'), data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(response.data['title'], "Some movie")

class SeatViewSetTest(APITestCase):
    def setUp(self):
        self.movie = Movie.objects.create(title="Title", description="desc", release_date=timezone.now(), duration=90)

    def test_seat_list(self):
        response = self.client.get(reverse('seat-list'))
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 20)

class BookingViewSetTeast(APITestCase):
    def setUp(self):
        self.movie = Movie.objects.create(title="Title", description="desc", release_date=timezone.now(), duration=90)
        self.seat = Seat.objects.get(movie=self.movie, seat_number=5)

    def test_booking_history(self):
        response = self.client.get(reverse('booking-history'))
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 0) 

        booking_url = reverse('seat-book-seat', kwargs={'pk': self.seat.pk})
        self.client.post(booking_url)
        response = self.client.get(reverse('booking-history'))
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 1)
        self.assertEqual(response.data[0]['seat'], self.seat.pk)