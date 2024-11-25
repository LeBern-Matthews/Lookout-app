import tkinter as tk
from tkinter import ttk
import public_ip as ip
import requests

root=tk.Tk()
BACKGROUND="#878672"

def main():
    
    root.geometry("360x640")
    #IP=getIP()
    #getcountry(IP)
    layout()
   
    root.resizable(False, False)
    root.mainloop()
    
def layout():
    navbar=tk.Frame(root, bg=BACKGROUND, height=200)
    btn=tk.Button(navbar, height=5,width=400, bg=BACKGROUND, activebackground=BACKGROUND, relief="flat", bd=0)
    btn.pack()
    navbar.place(x=-1,y=600)
    

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
       return 'Failed to retrieve info'
        
        
def weather_status():
    pass
    
if __name__=="__main__":
    main()