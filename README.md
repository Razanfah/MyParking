# MyParking 

A simple Streamlit app to manage parking slots, reservations, and cancellations.

## Features
- User-Friendly Interface: A simple and intuitive interface for managing parking spaces.
- Session State Management: Utilizes Streamlit's session state to manage parking slot availability.
- Invoice Generation: Automatically generates an invoice upon successful reservation.
- Dynamic Updates: Users can add new parking slots and view current parking status.

## Installation

1. Clone the repository or download the code:
    ```bash
    git clone https://github.com/Razanfah/MyParking.git
    ```

2. Install the required packages:
    ```bash
    pip install streamlit
    ```

3. Run the app:
    ```bash
    streamlit run app.py
    ```

## Code Overview

### Main Components
- Styling: Custom CSS is applied to enhance the user interface.
- Parking Slot Management: Logic to handle the reservation, cancellation, and addition of parking slots.
- Invoice Calculation: A function to calculate the price based on the number of hours reserved.

### Key Functions
- calculate_price(hours): Calculates the total price based on the number of hours parked.
- book_parking_slot(plate_number, hours): Reserves a parking slot and generates an invoice.
- cancel_booking(plate_number): Cancels a reservation based on the car's plate number.
- add_parking_slot(): Adds a new parking space to the system.
- search_car(plate_number): Searches for a parked car using the plate number.

## Usage
- Reserve a Parking Space: Input the car's plate number and the number of hours to reserve.
- Cancel a Reservation: Enter the plate number of the car to cancel its reservation.
- Add a New Parking Space: Click to add a new available parking slot.
- View Parking Status: Check the current status of all parking spaces.
- Search for a Parked Car: Find out where a specific car is parked by entering its plate number.