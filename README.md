 Overview
This milestone focuses on creating database models, serializers, and seeders for the Travel App.
It builds on Milestone 1 by defining the data structure and preparing the database with sample data.

🛠️ Features Implemented
1️⃣ Models
Listing: Stores property details (title, description, price, location).

Booking: Stores booking details for each listing.

Review: Stores user reviews for each listing.

2️⃣ Serializers
ListingSerializer: Converts Listing model to JSON.

BookingSerializer: Converts Booking model to JSON.

3️⃣ Seeder
Management command seed to populate the database with 10 sample listings and a demo user.