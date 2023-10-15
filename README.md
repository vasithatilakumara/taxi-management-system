# Taxi Management System (Python OOP Project)

## Overview
This project is a **menu-driven Taxi Management System** developed as part of my Master's coursework in Python programming.  
It demonstrates principles of **object-oriented programming (OOP)**, **file handling**, and **error management**.

## Features
- **Customer Management**
  - Basic and Enterprise customer types
  - Discounts and threshold-based pricing
- **Trip Booking**
  - Multi-destination trips
  - Cost calculation (base fee, distance fee, discounts, extra services)
  - Customizable rate types (standard, peak, weekend, holiday)
- **Services & Packages**
  - Add-ons such as Internet, Snacks, Drinks
  - Bundled service packages with discounts
- **Administration**
  - Add/update rate types
  - Add new locations
  - View customer booking history
  - Display the most valuable customer
- **File Persistence**
  - All customer, location, rate, and booking data are stored in text files

## Tech Stack
- Python 3.x
- Text files for data persistence (no external libraries required)

## Project Structure
taxi-management-system/
│── data/ # Input/output data files
│── src/ # Source code
│── README.md # Documentation

## Usage
cd src
python taxi_management.py ../data/customers.txt ../data/locations.txt ../data/rates.txt ../data/services.txt ../data/bookings.txt

## Example
Booking a trip will generate a detailed receipt:

Taxi Receipt
-------------------------------
Name: Louis
Departure: Melbourne
Destination: Chadstone
Distance: 12.5 km
Rate: standard (AUD per km)
Extra Service: Internet
Service Price: 1.00 (AUD)

Basic Fee: 4.20
Distance Fee: 18.75
Discount: 1.87
-------------------------------
Total Cost: 22.08 AUD

## Learning Outcomes
- Applied object-oriented programming (inheritance, polymorphism, encapsulation).
- Built a menu-driven CLI application.
- Handled file-based data persistence.
- Implemented custom exceptions for robust error handling.


