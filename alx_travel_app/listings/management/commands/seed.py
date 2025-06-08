from django.core.management.base import BaseCommand
from listings.models import Listing
import random

class Command(BaseCommand):
    help = 'Seed the database with sample listings'

    def handle(self, *args, **kwargs):
        if Listing.objects.exists():
            self.stdout.write(self.style.WARNING('Listings already seeded. Skipping.'))
            return

        sample_titles = ['Cozy Cabin', 'Beachfront Bungalow', 'Mountain Retreat']
        sample_locations = ['Nairobi', 'Mombasa', 'Naivasha']

        for i in range(5):
            Listing.objects.create(
                title=random.choice(sample_titles),
                location=random.choice(sample_locations),
                price=random.randint(50, 500),
                description=f'Sample listing {i+1}'
            )

        self.stdout.write(self.style.SUCCESS('Successfully seeded listings data.'))

