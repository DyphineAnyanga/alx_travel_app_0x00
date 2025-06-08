from django.core.management.base import BaseCommand
from listings.models import Listing
import random

class Command(BaseCommand):
    help = 'Seed the database with sample listings'

    def handle(self, *args, **kwargs):
        sample_data = [
            {
                "title": "Seaside Villa",
                "location": "Mombasa, Kenya",
                "price": 9500.00,
                "description": "Beautiful seaside villa with ocean views.",
            },
            {
                "title": "Nairobi Studio",
                "location": "Nairobi, Kenya",
                "price": 5000.00,
                "description": "Cozy studio apartment in the heart of Nairobi.",
            },
            {
                "title": "Safari Camp",
                "location": "Maasai Mara, Kenya",
                "price": 12000.00,
                "description": "Luxury tented camp experience near the reserve.",
            },
        ]

        for item in sample_data:
            listing, created = Listing.objects.get_or_create(
                title=item['title'],
                defaults={
                    "location": item["location"],
                    "price": item["price"],
                    "description": item["description"],
                    "is_available": True
                }
            )
            if created:
                self.stdout.write(self.style.SUCCESS(f"Added listing: {listing.title}"))
            else:
                self.stdout.write(f"Listing '{listing.title}' already exists.")
