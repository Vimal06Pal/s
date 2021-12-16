from geopy.geocoders import Nominatim

from helper import get_place
# Create your tests here.
zipcode = "201301"

place = get_place(zipcode)
print(place)
