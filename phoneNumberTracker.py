import phonenumbers
from phonenumbers import geocoder, carrier
from geopy.geocoders import Nominatim

def track_phone_number(phone_number):
    # Parse the phone number
    parsed_number = phonenumbers.parse(phone_number)

    # Get country location
    location = geocoder.description_for_number(parsed_number, "en")

    # Get service provider (carrier)
    service_provider = carrier.name_for_number(parsed_number, "en")

    # Use geopy to get more details (Optional)
    geolocator = Nominatim(user_agent="geoapiExercises")
    location_details = geolocator.geocode(location, timeout=10) if location else None

    # Print Results
    print(f"Phone Number: {phone_number}")
    print(f"Country/Region: {location}")
    print(f"Carrier: {service_provider}")
    if location_details:
        print(f"Latitude: {location_details.latitude}, Longitude: {location_details.longitude}")

    # Example usage
    track_phone_number("+94703006969")  # Replace with any valid phone number