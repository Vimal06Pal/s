# Importing required module
from geopy.geocoders import Nominatim

# Using Nominatim Api
def get_place(zipcode):
    place=''
    geolocator = Nominatim(user_agent="geoapiExercises")
    location = geolocator.geocode(zipcode)
    str_location = str(location)
    place=str_location.split(',')[1] + '-' + zipcode
    return(place)



import datetime
now = datetime.datetime.now().strftime('%A')
print(now)
# print((now.strftime("%A"))=="Wednesday")

def offer(day):
    d={}
    if day =="Wednesday":
        d["saree"] = 10
    return(d)

# off  =offer(now.strftime("%A"))
# print(off)


# Zipocde input
# zipcode = "201301"
# place = get_place(zipcode)
# print(place)

# Using geocode()

# Displaying address details
# print("Zipcode:",zipcode)
# print("Details of the Zipcode:")
# print(location)
