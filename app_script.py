import tkinter as tk
from tkinter import ttk
import public_ip as ip
import requests


def main():
    root=tk.Tk()
    root.geometry("360x640")
    IP=getIP()
    getcountry(IP)
    
    
    root.mainloop()
    
def layout():
    pass

def getIP():
    # Python Program to Get IP Address
    
    IPAddr=ip.get()
    return str(IPAddr)

def getcountry(IP):
    # Define API URL
    print(IP)
    BASE_URL = 'https://apiip.net/api/check?ip='
    
    API_URL=BASE_URL+IP+'&accessKey=d4f9b109-0a44-4e29-8cdc-c66c07de1942'
    
    print(API_URL)
   
    # Getting in response JSON
    response = requests.get(API_URL)
    
    # Loading JSON from text to object
    json_response = response.json()
    
    if response.status_code==200:
        return json_response["countryName"]
    else:
        print('Failed to retrieve info')
        
        
def weather_status():
    pass
    
if __name__=="__main__":
    main()