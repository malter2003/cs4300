# Movie Booking System
Allows users to view a list of movies, view seat availability, and book seats. The API uses Django's REST framework.

Unit tests are in `reservations/tests.py` and integration tests are in `reservations/test_views.py`


### Setup
1. Clone the repo `git clone https://github.com/malter2003/cs4300`
2. Setup python virtual environment `python3 -m venv venv`, `source venv/bin/activate`
3. Setup migrations `python manage.py migrate`
4. Start the server `python manage.py runserver`
5. Access on localhost:8000
