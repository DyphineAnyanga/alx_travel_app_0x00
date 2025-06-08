from django.db import models

class Listing(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField()
    price = models.DecimalField(max_digits=10, decimal_places=2)
    location = models.CharField(max_length=255)

    def __str__(self):
        return self.title

class Booking(models.Model):
    listing = models.ForeignKey(Listing, on_delete=models.CASCADE, related_name='bookings')
    user_name = models.CharField(max_length=100)
    start_date = models.DateField()
    end_date = models.DateField()

    def __str__(self):
        return f"Booking by {self.user_name} for {self.listing.title}"

class Review(models.Model):
    listing = models.ForeignKey(Listing, on_delete=models.CASCADE, related_name='reviews')
    rating = models.IntegerField()
    comment = models.TextField()

    def __str__(self):
        return f"Review for {self.listing.title} - {self.rating}"

