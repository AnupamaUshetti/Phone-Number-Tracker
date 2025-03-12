import phonenumbers
from phonenumbers import geocoder, carrier
from phoneNumbers import number
import folium

key = "ee4ac5ef92d94272a37530e8c6a98bfd"

check_number = phonenumbers.parse(number)
number_location = geocoder.description_for_number(check_number, "en")
print(number_location)

service_provider = phonenumbers.parse(number)
print(carrier.name_for_number(service_provider, "en"))

from opencage.geocoder import OpenCageGeocode
geocoder = OpenCageGeocode(key)

query = str(number_location)
reults = geocoder.geocode(query)

latitude = reults[0]['geometry']['lat']
longitude = reults[0]['geometry']['lng']
print(latitude, longitude)

map_location = folium.Map(location = [latitude, longitude], zoom_start=5)
folium.Marker([latitude, longitude], popup=number_location).add_to(map_location)
map_location.save("location.html")