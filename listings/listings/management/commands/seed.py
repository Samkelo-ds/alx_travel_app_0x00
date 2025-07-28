from django.core.management.base import BaseCommand
from listings.models import Listing
from django.contrib.auth.models import User
import random


class Command(BaseCommand):
    help = 'Seed database with sample listings'

    def handle(self, *args, **kwargs):
        self.stdout.write("Seeding database...")

        # Create demo user if not exists
        if not User.objects.filter(username='demo').exists():
            User.objects.create_user(username='demo', password='demo1234')

        titles = ['Cozy Cottage', 'Modern Apartment', 'Beach House', 'Mountain Cabin']
        locations = ['Cape Town', 'Durban', 'Johannesburg', 'Pretoria']

        for _ in range(10):
            Listing.objects.create(
                title=random.choice(titles),
                description="Sample description for listing",
                price_per_night=round(random.uniform(500, 1500), 2),
                location=random.choice(locations)
            )

        self.stdout.write(self.style.SUCCESS("Database seeded successfully!"))
