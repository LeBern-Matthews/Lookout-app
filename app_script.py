import tkinter as tk
from tkinter import ttk
import socket
import requests


def main():
    root=tk.Tk()

   
    root.mainloop()
    
def layout():
    pass

def getIP():
    # Python Program to Get IP Address
    
    hostname = socket.gethostname()
    IPAddr = socket.gethostbyname(hostname)
    
    print("Your Computer Name is:" + hostname)
    print("Your Computer IP Address is:" + IPAddr)
    return IPAddr

def getcountry():
    # Define API URL
    API_URL = 'https://apiip.net/api/check?accessKey={905c0915-afc8-4dc5-a258-1243c62db6dd}'
    
    # Enter the ip for search
    IP_FOR_SEARCH = '&ip=67.250.186.196'
    
    # Getting in response JSON
    response = requests.get(API_URL+IP_FOR_SEARCH)
    
    # Loading JSON from text to object
    json_response = response.json()
    
    # Print the results
    print(json_response)
    if json_response==200:
        print(json_response["countryName"])
    
def weather_status():
    pass
    
if __name__="main":
    main():
