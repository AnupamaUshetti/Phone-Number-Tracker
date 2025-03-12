import phonenumbers
from phonenumbers import geocoder
from phoneNumbers import number
import folium

check_number = phonenumbers.parse(number)
number_location = geocoder.description_for_number(check_number, "en")
print(number_location)

