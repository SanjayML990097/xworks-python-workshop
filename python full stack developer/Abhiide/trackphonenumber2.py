import phonenumbers
from phonenumbers import geocoder
from test import number4
import folium
check_number = phonenumbers.parse(number4)
number_location = geocoder.description_for_number(check_number,"en")
print(number_location)

