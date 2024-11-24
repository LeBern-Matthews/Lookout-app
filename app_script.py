import tkinter as tk
from tkinter import ttk
import socket
import requests


def main():
    root=tk.Tk()
    IP=getIP()
    getcountry(IP)
    root.mainloop()
    
def layout():
    pass

def getIP():
    # Python Program to Get IP Address
    
    hostname = socket.gethostname()
    IPAddr = socket.gethostbyname(hostname)
    
    print("Your Computer IP Address is:" + IPAddr)
    return IPAddr

def getcountry(IP):
    # Define API URL
    API_URL = 'https://apiip.net/api/check?accessKey={d4f9b109-0a44-4e29-8cdc-c66c07de1942}'
    
    # Enter the ip for search
    IP_FOR_SEARCH = '&ip='+IP
    
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
    
if __name__=="__main__":
    main()