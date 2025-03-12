import phonenumbers
from phonenumbers import geocoder
import folium
from geopy.geocoders import Nominatim
import tkinter as tk
from tkinter import messagebox

def track_phone_number():
    phone_number = entry.get()  # Get input from user
    if not phone_number:
        messagebox.showerror("Error", "Please enter a phone number")
        return

    try:
        # Parse the phone number
        parsed_number = phonenumbers.parse(phone_number)

        # Get country location
        location = geocoder.description_for_number(parsed_number, "en")

        # Get service provider (carrier)
        service_provider = carrier.name_for_number(parsed_number, "en")

        # Use geopy to get more details (Optional)
        geolocator = Nominatim(user_agent="geoapiExercises")
        location_details = geolocator.geocode(location, timeout=10) if location else None

        # Display Results
        result_text = f"Phone Number: {phone_number}\n"
        result_text += f"Country/Region: {location}\n"
        result_text += f"Carrier: {service_provider}\n"

        if location_details:
            result_text += f"Latitude: {location_details.latitude}, Longitude: {location_details.longitude}\n"

        result_label.config(text=result_text)
    
    except Exception as e:
        messagebox.showerror("Error", f"Invalid phone number\n{e}")

# Create GUI window
root = tk.Tk()
root.title("Phone Number Tracker")
root.geometry("400x300")

# Input field
tk.Label(root, text="Enter Phone Number:", font=("Arial", 12)).pack(pady=10)
entry = tk.Entry(root, width=30, font=("Arial", 12))
entry.pack(pady=5)

# Button
track_button = tk.Button(root, text="Track", font=("Arial", 12), command=track_phone_number)
track_button.pack(pady=10)

# Result Label
result_label = tk.Label(root, text="", font=("Arial", 12), justify="left")
result_label.pack(pady=10)

# Run GUI
root.mainloop()