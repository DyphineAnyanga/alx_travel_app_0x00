from django.core.management.base import BaseCommand
from listings.models import Listing

class Command(BaseCommand):
    help = 'Seed the database with sample listings data'

    def handle(self, *args, **kwargs):
        Listing.objects.create(title="Test Listing", description="Just a test", price=100)
        self.stdout.write(self.style.SUCCESS('Successfully seeded data.'))
