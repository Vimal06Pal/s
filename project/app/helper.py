# Importing required module
from geopy.geocoders import Nominatim

# Using Nominatim Api
def get_place(zipcode):
    place=''
    geolocator = Nominatim(user_agent="geoapiExercises")
    location = geolocator.geocode(zipcode)
    str_location = str(location)
    if str_location.split(',')[-1] ==" India":
        place=str_location.split(',')[1] + '-' + zipcode
        return(place)
    else:
        return('')



import datetime
now = datetime.datetime.now().strftime('%A')
# print(now)
# print((now.strftime("%A"))=="Wednesday")

def offer(day):
    d={}
    if day == "Monday":
        pass
    elif day == "Tuesday":
        d["saree"] = 10
    elif day =="Wednesday":
        pass
    elif day == "Thursday":
        pass
    elif day == "Friday":
        pass
    elif day == "Saturday":
        pass
    elif day =="Sunday":
        pass
    else:
        pass
    return(d)
    # else:
    #     return(0)

# off  =offer(now.strftime("%A"))
# print(off)


# Zipocde input
# zipcode = "201301"
# place = get_place(zipcode)
# print((place[4])==" India")

# Using geocode()

# Displaying address details
# print("Zipcode:",zipcode)
# print("Details of the Zipcode:")
# print(location)
