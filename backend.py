from tkinter import PhotoImage as PImage, Tk
import json
from socket import create_connection
from requests import get
from datetime import datetime
from public_ip import get as ip
from os import path

root=Tk()

def initialise_constants():
    global BACKGROUND, DARKBACKGROUND, NAVBAR_BACKGROUND, DARK_NAVBAR_BACKGROUND, GREEN, YELLOW, RED
    
    # COLOURS
    BACKGROUND="#f4f0dc"
    DARKBACKGROUND="#1e1e1e"
    NAVBAR_BACKGROUND="#6d6a42"
    DARK_NAVBAR_BACKGROUND="#545333"
    GREEN="#357C3C"
    YELLOW="#FFD700"
    RED="#990000"
    
    global home_icon, user_icon, contacts_icon, checklist_icon, home_icon_white, user_icon_white, contacts_icon_white, checklist_icon_white, root_image

    # ICONS
    home_icon=PImage(file="pictures/home.png")
    user_icon=PImage(file="pictures/setting.png")
    contacts_icon=PImage(file="pictures/id-card.png")
    checklist_icon=PImage(file="pictures/test.png")

    # ICONS WHITE
    home_icon_white=PImage(file="pictures/home-white.png")
    user_icon_white=PImage(file="pictures/setting-white.png")
    contacts_icon_white=PImage(file="pictures/id-card-white.png")
    checklist_icon_white=PImage(file="pictures/test-white.png")

    #root image
    root_image=PImage(file="pictures/icon.png")
    
def get_essentials()->list:
    """
    Returns a list of essential items for the user to pack for a hurricane from the file "essetial_items.txt"
    """
    with open ("essetial_items.txt", "r") as file:
        essentials=[line.strip() for line in file]
        return essentials

def country_options()->list:
    """
    Returns a list of supported countries
    """
    options = [ 
        "Anguilla", 
        "Antigua and Barbuda", 
        "Bahamas", 
        "Barbados", 
        "Belize", 
        "Bermuda", 
        "Bonaire",
        "British Virgin Islands",
        "Cayman Islands",
        "Cuba",
        "Curacao",
        "Dominica",
        "Grenada",
        "Guadeloupe",
        "Jamaica",
        "Martinique",
        "Montserrat",
        "Puerto Rico",
        "Saba",
        "Saint Barthélemy",
        "Saint Kitts and Nevis",
        "Saint Lucia",
        "Saint Martin",
        "Saint Vincent and the Grenadines",
        "Eustatius",
        "Trinidad and Tobago",
        "Turks and Caicos Islands"
    ]
    return options

def check_month(number:str)->str:
    """
    Takes in an integer and returns a string coresponding to the month
    """
    number=int(number)

    match number:
        case 1:
            month="January"
        case 2:
            month="February"
        case 3:
            month="March"
        case 4:
            month="April"
        case 5:
            month="May"
        case 6:
            month="June"
        case 7:
            month="July"
        case 8:
            month="August"
        case 9:
            month="September"
        case 10:
            month="October"
        case 11:
            month="November"
        case 12:
            month="December"
    return month

def weather_status(location_info:dict) -> str | dict:
    """
    Gets the weather and temperature of a location based on the latitude and longitude
    """
    API_KEY="1fb077c200d03c89456700827a2db657"
    lat=location_info["latitude"]
    lon=location_info["longitude"]

    weather_data = get(f"https://api.openweathermap.org/data/2.5/weather?lat={lat}&lon={lon}&appid={API_KEY}&units=metric")

    if weather_data.json()['cod'] == 200:
        weather = weather_data.json()['weather'][0]['main']
        weather_description = weather_data.json()['weather'][0]['description']
        temp = round(weather_data.json()['main']['temp'])
    
        weather_info ={
            "weather":weather,
            "temp":temp,
            "description":weather_description,
            "time": datetime.now().strftime(r'%H:%M,%d:%m:%y')
        }
        with open('weather_info.json', 'w') as file:
            file.write(json.dumps(weather_info))
        return weather_info
    else:
        return 'Failed to retrieve info'

def has_internet_connection()->bool:
    """
    Checks if the device has an active internet connection.
    
    Returns:
        bool: True if connected to the internet, False otherwise.
    """
    try:
        # Try connecting to a public domain (like google.com)
        create_connection(("8.8.8.8", 53)) 
        return True
    except Exception:
        return False

def getcountry(IP:str)->str:
    """
    Finds the country name based on the IP adress entered

    Args:
        IP (str): Public IP address (IPv4 or IPv6)

    Returns:
        dict: Dictionary containing the country name, latitude and 

        location_info=
        {
        "country":    json_response["officialCountryName"],
        "latitude":   json_response["latitude"],
        "longitude":  json_response["longitude"]
        }
        str: "failed to retrieve info" if the request fails
    """
    # Define API URL
    BASE_URL = 'https://apiip.net/api/check?ip='
    
    API_URL=BASE_URL+IP+'&accessKey=d4f9b109-0a44-4e29-8cdc-c66c07de1942'
   
    # Getting in response JSON
    response = get(API_URL)
    
    # Loading JSON from text to object
    json_response = response.json()
    
    if response.status_code==200:
        location_info={
            "country":json_response["officialCountryName"],
            "latitude":json_response["latitude"],
            "longitude":json_response["longitude"]
        }
        return location_info
    else:
       return 'Failed to retrieve info'

def emergency_contacts(Country_name:str)->dict:
    """
    Retrieves emergency contacts from "country.json" based on the country name entered

    Args:
        Country_name (str): A string containing the name of the country program is being ran in

    Returns:
        dict: Dictionary containing the countries, the key, and emergency contacts as the argument
    """
    with open("country_data.json", "r") as file:
        x:dict=json.load(file)# dictionary containing the countries and their emergency contacts
        for country in x["countries"]:
            for place, value in country.items():
                if place==Country_name:
                    country_info={place:value}
                    return country_info

def getIP()->str:
    """
    Gets Ip dress from the public_ip module

    Returns:
        str: IP adress in string form
    """
    # Python Program to Get IP Address
    
    IPAddr=ip()
    return str(IPAddr)

def weather_stuff():
    global weather, temp, description, last_updated_msg, last_updated_time, Country_name, text
    if has_internet_connection():
        IP=getIP()
        location_info:dict=getcountry(IP)
        Country_name=location_info["country"]
        text=Country_name
        weather_stuff=weather_status(location_info)
        weather=f"Current weather is {weather_stuff["weather"]}"
        temp="Temperature: "+str(weather_stuff["temp"])+"°C"
        description=f"Weather description: {weather_stuff["description"]}"
        last_updated_time=weather_stuff["time"]
        time_part,date_part=last_updated_time.split(",")
        month=check_month(date_part[3:5])
        
        date=f"{int(date_part[0:2])}th of {month}, 20{int(date_part[6:8])}"

        if time_part[0:2]>"12":
            time_part=f"{int(time_part[0:2])-12}:{time_part[3:5]} PM"
        else:
            time_part=f"{time_part} AM"

        last_updated_msg=f"{time_part} on {date}"

    else:
        Country_name="Select a county in settings"
        text="Choose location"

        if path.exists("weather_info.json"):
            with open("weather_info.json", "r") as file:
                x:dict=json.load(file)
                last_updated_time=x["time"]
                
                weather=f"Current weather is {x["weather"]}"
                temp="Temperature: "+str(x["temp"])+"°C"
                description=f"Weather description: {x["description"]}"

                time_part,date_part=last_updated_time.split(",")
                month=check_month(date_part[3:5])
                
                date=f"{int(date_part[0:2])}th of {month}, 20{int(date_part[6:8])}"

                if time_part[0:2]>"12":
                    time_part=f"{int(time_part[0:2])-12}:{time_part[3:5]} PM"
                else:
                    time_part=f"{time_part} AM"

                last_updated_msg=f"{time_part} on {date}"
        else:
            last_updated_msg="No previous data"
            weather=""
            temp=""
            description=""

initialise_constants()
weather_stuff()