from django.test import TestCase
from django.contrib.auth.models import User
from .models import Listing, Booking
from django.core.management import call_command

class ListingModelTest(TestCase):
    def setUp(self):
        self.listing = Listing.objects.create(
            title="Test Listing",
            description="Description",
            price_per_night=1000,
            location="Cape Town"
        )

    def test_listing_creation(self):
        self.assertEqual(self.listing.title, "Test Listing")


class SeederTest(TestCase):
    def test_seed_command(self):
        call_command('seed')
        self.assertTrue(Listing.objects.count() >= 10)


class BookingModelTest(TestCase):
    def setUp(self):
        self.user = User.objects.create_user(username='testuser', password='12345')
        self.listing = Listing.objects.create(
            title="Test Booking Listing",
            description="Booking description",
            price_per_night=800,
            location="Durban"
        )
        self.booking = Booking.objects.create(
            user=self.user,
            listing=self.listing,
            check_in="2025-08-01",
            check_out="2025-08-05",
            guests=2
        )

    def test_booking_creation(self):
        self.assertEqual(self.booking.guests, 2)
