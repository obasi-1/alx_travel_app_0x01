# Alx_travel_app_0x01

# ALX Travel App

This repository, alx_travel_app_0x01, is an extension of the alx_travel_app_0x00 project, focusing on the implementation of a RESTful API for managing listings and bookings.

The API is built using the Django REST framework and provides full CRUD (Create, Read, Update, Delete) functionality for both the Listing and Booking models.

# API Endpoints

The API is accessible under the /api/ path and is automatically documented using Swagger.

Listings Endpoints:

GET /api/listings/: Retrieve a list of all listings.

POST /api/listings/: Create a new listing.

GET /api/listings/{id}/: Retrieve the details of a single listing.

PUT /api/listings/{id}/: Update an entire listing.

PATCH /api/listings/{id}/: Partially update a listing.

DELETE /api/listings/{id}/: Delete a listing.

Bookings Endpoints:

GET /api/bookings/: Retrieve a list of all bookings.

POST /api/bookings/: Create a new booking.

GET /api/bookings/{id}/: Retrieve the details of a single booking.

PUT /api/bookings/{id}/: Update an entire booking.

PATCH /api/bookings/{id}/: Partially update a booking.

DELETE /api/bookings/{id}/: Delete a booking.

# API Documentation with Swagger

To view the interactive API documentation, you need to install drf-yasg:

pip install drf-yasg

Then, run your Django development server:

python manage.py runserver

You can access the Swagger UI documentation at http://127.0.0.1:8000/swagger/ and the ReDoc documentation at http://127.0.0.1:8000/redoc/.

This setup provides a comprehensive and easy-to-use interface for developers to interact with and understand the API.
