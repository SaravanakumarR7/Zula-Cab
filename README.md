# 🚖 Zula Booking App

    **Zula Booking App** is a **cab booking system** built in Python (LLD – Low Level Design).
    It models how cab platforms like Ola/Uber work by handling **Passengers**, **Drivers**, and **Admins** with **dynamic taxi allocation, fare calculation, and trip history tracking**.

## ✨ Features

    ### 👤 Passenger
    
        * Register & log in (passwords stored securely with SHA-256)
        * **Hail or Book a Taxi** (nearest cab auto-assigned)
        * Location updates after each ride
        * Ride history (source, destination, cab details, fare)
        * Edit profile (name/password)

    ### 🚕 Driver
    
        * Register & log in (with password encryption)
        * Auto-assigned to nearest passenger requests
        * Track **earnings, Zula commission, and total trips**
        * Location updates after each trip
        * View ride history (passenger IDs, fares, commissions)
        * Edit profile (name/password)

    ### 👨‍💻 Admin
        
        * Secure admin login
        * View **driver details** (earnings, trips, commission, login status)
        * View **passenger details** (login status, trips taken)
        * View ride histories (drivers & passengers)
        * Remove drivers from the system

## ⚙️ How It Works

    * Fixed route points `A–H` mapped to distances.
    * **Fare Formula:**
    
      ```
          Fare = (Distance to passenger + Distance to destination) × 10
      ```
    * **Revenue Split:**
    
          * Driver earns **70%**
          * Zula keeps **30% commission**
          
    * **Cab Allocation Rules:**
    
          1. Nearest driver is chosen
          2. If tie → driver with fewer trips is selected

## 📂 Project Structure

```
├── Booking.py          # Ride handling, cab allocation, fare calculation
├── Cab_Driver.py       # Driver class (SHA-256 password encryption)
├── Driver_login.py     # Driver login system
├── Passenger_login.py  # Passenger login system
├── Passengers.py       # Passenger class (SHA-256 password encryption)
├── Main.py             # Entry point, system flow
```

1. Run the program:

       ```bash
       python Main.py
       ```

2. Use the interactive flow to:

       * Sign up (Driver/Passenger)
       * Log in
       * Hail or Book rides
       * View ride histories
       * Access Admin functions
       * Edit profiles

## 🔒 Security

    * Passwords stored using **SHA-256 hashing** (not plain text).
    * Only logged-in users can book rides or edit profiles.
    * Admin has separate secure credentials.
    
## 🛠️ Future Enhancements

    * Web app interface (Flask/Django + React)
    * GPS & Maps integration
    * Online payment support
    * Push notifications for rides

## 👨‍💻 Author

    Developed by **Saravanakumar R** 🚀
