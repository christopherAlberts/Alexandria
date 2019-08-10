import json
import os
import urllib.request
from math import cos,sin,sqrt
import tableformatter as tf
from datetime import datetime

def clean_up(x1, x2, x3):

    # x1 = Variable
    # x2 = will start cutting just after this point
    # x3 = Will cut just before this point

    short_response = x1[x1.index(x2)+len(x2):len(x1)]
    start_point = 0
    end_point = short_response.index(x3)
    clean_response = short_response[start_point:end_point]
    return clean_response


def url_response(x1):

    #  x1 = the url that
    response = urllib.request.urlopen(x1)
    full_response = json.loads(response.read())
    return full_response


def iss_loop():

    # This code will loop the iss() function until Ctrl-c is pressed
    try:
        while True:
            iss()
    except KeyboardInterrupt:  # Ctrl-c will end the program.
        pass


# This is the main portion of the code:
def iss():
    # Get your IPSTACK TOKEN here: https://ipstack.com/
    ipstack_token = "171bded87705d73d11cd9e70d4c2cd64"  # Add your ipstack token here
    url_ipstack = ('http://api.ipstack.com/102.65.204.221?access_key=' + ipstack_token)

    ipstack = url_response(url_ipstack)
    my_lon = clean_up(str(ipstack), "longitude\': ", ",")
    my_lat = clean_up(str(ipstack),"latitude\': ", ",")

    url_iss_people = 'http://api.open-notify.org/astros.json'
    iss_people = url_response(url_iss_people)
    num_people = clean_up(str(iss_people), "number\': ", "}")

    url_iss_location = 'http://api.open-notify.org/iss-now.json'
    iss_location = url_response(url_iss_location)
    iss_lon = clean_up(str(iss_location), "longitude': \'", "\'")
    iss_lat = clean_up(str(iss_location), "latitude': \'", "\'")

    url_iss_pass_time = 'http://api.open-notify.org/iss-pass.json?lat=' + str(my_lat) + '&lon=' + str(my_lon)
    iss_pass = url_response(url_iss_pass_time)
    num_passes_today = clean_up(str(iss_pass), "passes': ", "}")

    # DISTANCE TO INTERNATIONAL SPACE STATION CALCULATION:
    r = 6371  # Radius of the Earth in km
    b = 408  # Height of the International Space Station in km

    t = (r + b) * sin(float(my_lat) - float(iss_lat))
    x = (r + b) * cos(float(my_lat) - float(iss_lat))
    s2 = ((r ** 2) + (x ** 2)) - (2 * (r * x)) * cos(float(my_lon) - float(iss_lon))
    t2 = t * t

    finale_distance = sqrt(s2 + t2)
    finale_distance = round(finale_distance, 2)

    # The following line of code: will check the systems OS
    # and then execute the appropriate command to clear the screen.
    os.system('cls' if os.name == 'nt' else 'clear')

    print("########################################")
    print("      International Space Station")
    print("########################################")
    print("----------------------------------------")
    print("\t   You are currently \n\t  "
          " >>> " + str(finale_distance) + "km <<<\n" +
          " from the International Space Station.")
    print("----------------------------------------")

    # My & International Space Station LATITUDE AND LONGITUDE
    cols = ['', 'Latitude', 'Longitude']
    rows = [('Your location', my_lat, my_lon), ("ISS location", iss_lat, iss_lon)]
    print(tf.generate_table(rows, cols))
    print("----------------------------------------")
    print(" The International Space Station will\n "
          "be passing over you " + num_passes_today +
          " times today.")
    print("----------------------------------------")

    # Internationa Space Station PASSING TIME
    pass_row = []
    s = 0
    while s <= int(num_passes_today)-1:
        num = []
        pass_array = []
        risetime_array = []
        duration_array = []
        passover = iss_pass.get("response")
        risetime = passover[s].get("risetime")
        duration = passover[s].get("duration")
        duration = round(duration / 60,2)
        risetime = datetime.fromtimestamp(risetime)
        num.append(s + 1)
        duration_array.append(duration)
        risetime_array.append(risetime)
        row_array = num + duration_array + risetime_array
        pass_row.append(row_array)
        s += 1

    pass_col = ['Number', 'Duration', 'Risetime']
    print(tf.generate_table(pass_row, pass_col))

    print("----------------------------------------")
    print(" There are currently " + num_people +
          " people in space.")
    print("----------------------------------------")

    # International Space Station PEOPLE
    people_row = []
    m = 0
    while m <= int(num_people)-1:
        people_array = []
        craft_array = []
        num = []
        people = iss_people.get("people")
        people = people[m].get("name")
        craft = iss_people.get("people")
        craft = craft[m].get("craft")
        people_array.append(people)
        craft_array.append(craft)
        num.append(m+1)
        row = num + people_array + craft_array
        people_row.append(row)
        m += 1

    people_col = ['Number', 'Astronauts', 'Craft']
    print(tf.generate_table(people_row,people_col))

iss()
# iss_loop()
