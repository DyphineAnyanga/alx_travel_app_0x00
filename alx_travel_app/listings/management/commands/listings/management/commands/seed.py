from django.core.management.base import BaseCommand
from listings.models import Listing

class Command(BaseCommand):
    help = "Seed the database with sample listings data"

    def handle(self, *args, **kwargs):
        # Clear existing data
        Listing.objects.all().delete()

        # Sample data
        sample_listings = [
            {
                "title": "Lakeview Cabin",
                "description": "A beautiful cabin with a view of the lake.",
                "price": 150.00,
                "location": "Lake Victoria",
            },
            {
                "title": "Mountain Retreat",
                "description": "A peaceful house in the mountains.",
                "price": 180.00,
                "location": "Mount Elgon",
            },
            {
                "title": "Urban Studio",
                "description": "A compact studio apartment in the city.",
                "price": 95.00,
                "location": "Nairobi",
            },
        ]

        for data in sample_listings:
            Listing.objects.create(**data)

        self.stdout.write(self.style.SUCCESS('Successfully seeded listings data.'))
