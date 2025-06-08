#!/bin/bash

# 1. Check README.md (must exist and not empty)
if [ -s README.md ]; then
  echo "README.md exists and is not empty"
else
  echo "Creating README.md with starter content"
  cat << EOF > README.md
# ALX Travel App 0x00

This project involves creating models, serializers, and seeders for the ALX Travel App.

## Project Setup

- Django REST Framework for API
- Models: Listing, Booking, Review
- Seeders to populate sample data

EOF
fi

# 2. Check listings/models.py (must exist and be empty)
mkdir -p listings

if [ -e listings/models.py ]; then
  if [ ! -s listings/models.py ]; then
    echo "listings/models.py exists and is empty"
  else
    echo "Clearing contents of listings/models.py to be empty"
    > listings/models.py
  fi
else
  echo "Creating empty listings/models.py"
  > listings/models.py
fi

# 3. Check listings/serializers.py (must exist and not empty)
if [ -s listings/serializers.py ]; then
  echo "listings/serializers.py exists and is not empty"
else
  echo "Creating listings/serializers.py with starter content"
  cat << EOF > listings/serializers.py
from rest_framework import serializers
from .models import Listing, Booking

class ListingSerializer(serializers.ModelSerializer):
    class Meta:
        model = Listing
        fields = '__all__'

class BookingSerializer(serializers.ModelSerializer):
    class Meta:
        model = Booking
        fields = '__all__'

EOF
fi

echo "Setup complete."
