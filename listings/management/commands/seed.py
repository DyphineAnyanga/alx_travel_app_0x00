from django.core.management.base import BaseCommand
from listings.models import Listing

class Command(BaseCommand):
    help = 'Seed the database with sample listings'

    def handle(self, *args, **kwargs):
        sample_listings = [
            {'title': 'Beach House', 'description': 'A lovely beach house', 'price': 150.00, 'location': 'Malindi'},
            {'title': 'Mountain Cabin', 'description': 'Cozy cabin in the mountains', 'price': 100.00, 'location': 'Kisumu'},
            {'title': 'City Apartment', 'description': 'Modern apartment downtown', 'price': 200.00, 'location': 'Nairobi'},
        ]

        for listing_data in sample_listings:
            Listing.objects.create(**listing_data)
        
        self.stdout.write(self.style.SUCCESS('Successfully seeded the database with listings'))

