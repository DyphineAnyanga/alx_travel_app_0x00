from django.core.management.base import BaseCommand
from listings.models import Listing

class Command(BaseCommand):
    help = 'Seed database with sample listings'

    def handle(self, *args, **kwargs):
        listings = [
            {"title": "Cozy Cottage", "description": "A cozy place to stay.", "location": "Nairobi", "price_per_night": 50.00},
            {"title": "Beachfront Villa", "description": "A luxurious villa near the ocean.", "location": "Mombasa", "price_per_night": 120.00}
        ]

        for item in listings:
            Listing.objects.create(**item)

        self.stdout.write(self.style.SUCCESS("Database seeded successfully"))

