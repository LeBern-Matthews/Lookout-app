import tkinter as tk
from tkinter import ttk
import public_ip as ip
import requests
import json

root=tk.Tk()
#BACKGROUND="#878672"
BACKGROUND="#545333"
home_icon=tk.PhotoImage(file=r"home.png")
user_icon=tk.PhotoImage(file=r"user.png")
contacts_icon=tk.PhotoImage(file=r"id-card.png")
Checklist_icon=tk.PhotoImage(file=r"test.png")

essentials=["Water: 1 gallon per person, per day, for at least 3 days", "Non-perishable Food: Canned goods, dries fruits, nuts", "Manual can opener", "First-Aid kit", "Battery-powered or hand-cranked rdio", "Flashlights and extra betteries", "Cell phone charger", "Cash: ATMs may be unavailable", "Important documents: Birth Certificates, insurance policies","Tools", "Hygiene Items", "Wet wipes", "Plastic bags", "work gloves", "Blackets and Pillows", "Rain Gear"]
progresss_fill:int=0

def main():
    root.title("Lookout")
    root.geometry("360x640")
    
    IP=getIP()
    Country_name=getcountry(IP)
    layout(Country_name)
    root.resizable(False, False)
    center_window(root)
    root.mainloop()

def center_window(window):
    window.update_idletasks()
    width = window.winfo_width()
    height = window.winfo_height()
    screen_width = window.winfo_screenwidth()
    screen_height = window.winfo_screenheight()
    x = (screen_width - width) // 2
    y = (screen_height - height) // 2
    window.geometry(f"{width}x{height}+{x}+{y}")

def layout(Country_name:str):
    main_frame=tk.Frame(root, highlightbackground="black", highlightthickness=2) 
    main_frame.pack_propagate(False)
    main_frame.configure(height=560, width=360)
    
    main_frame.pack(side="top")
    

    def fill_progressbar():
        global progresss_fill

        progresss_fill+=6
        print("Entered fill_progressbar")
        Progress_bar.configure(value=progresss_fill)
        print("Updated progress bar", progresss_fill)
        root.update_idletasks()


    # HOME PAGE
    
    home_frame=tk.Frame(main_frame, highlightbackground="black", highlightthickness=2,height=1000, width=360)
    home_frame.winfo_id()

    new_style=ttk.Style()
    new_style.configure("Bad.Horizontal.TProgressbar",background='#52593b')
    new_style.configure("Moderate.Horizontal.TProgressbar",background='#52593b')
    new_style.configure("Good.Horizontal.TProgressbar",background='#52593b')

    Progress_bar=ttk.Progressbar(home_frame, orient="horizontal", length=300, mode="determinate", style="Custom.Horizontal.TProgressbar")
    
    preparedness_meter=tk.Label(home_frame, text="Prepared-o-meter", font="Bold, 24")
    weather_lbl=tk.Label(home_frame, font="Bold, 12",text="Weather")

    preparedness_meter.pack(pady=5)
    Progress_bar.pack(padx=0, pady=5)
    weather_lbl.place(y=265, x=0)
    home_frame.pack_propagate(False)
    home_frame.pack()
    
    # CHECKLIST PAGE
    checklist_frame=tk.Frame(main_frame, highlightbackground="black", highlightthickness=2,height=560, width=360) 
    checklist_frame.pack_propagate(False)
    
    essential_supplies=tk.Label(checklist_frame, text="Essential supplies", font=("Bold",  16, "underline"))
    essential_supplies.place(x=0, y=5)
    
    essentials_frame=tk.Frame(checklist_frame)
    for essential in essentials:
        check_btn=tk.Checkbutton(essentials_frame, text=f"{essential}", height=1, command=fill_progressbar)
        check_btn.pack_configure(pady=2,anchor="w")
    essentials_frame.place(x=0, y=70)
    
    checklist_frame.pack()

    """
    Creats an emergency contacts page which displays the police, ambulance and fire department contacts
    """
    contacts_frame=tk.Frame(main_frame, highlightbackground="black", highlightthickness=2,height=560, width=360)
    contacts_frame.pack_propagate(False)
    lb=tk.Label(contacts_frame, text="EMERGENCY CONTACTS", font="Bold, 20")
    lb.pack(pady=10)
    for_country=tk.Label(contacts_frame, text=f"For {Country_name}", font="Bold, 14")
    for_country.pack(anchor="w")
    services=emergency_contacts(Country_name)

    # adjsting for multiple numbers
    if type(services[Country_name]["police"])== list:
        police_number=""
        for number in services[Country_name]["police"]:
            police_number=f"{police_number},{number}"

    else:
        police_number=services[Country_name]["police"]

    # creating label for the Police number
    police_lbl=tk.Label(contacts_frame, text=f"Police: {police_number}", font="Bold, 12")
    police_lbl.pack(anchor="w", pady=5)
    
    # adjsting for multiple numbers        
    if type(services[Country_name]["ambulance"])== list:
        ambulance_number=""
        for number in services[Country_name]["ambulance"]:
            ambulance_number=f"{ambulance_number},{number}"
    else:
        ambulance_number=services[Country_name]["ambulance"]

    # creating label for the Ambulance numbers
    ambulance_lbl=tk.Label(contacts_frame, text=f"Ambulance: {ambulance_number}", font="Bold, 12")
    ambulance_lbl.pack(anchor="w", pady=5)

    # adjsting for multiple numbers
    if type(services[Country_name]["fire_dept"])== list:
        fire_dept_number=""
        for number in services[Country_name]["fire_dept"]:
            fire_dept_number=f"{fire_dept_number},{number}"
    else:
        fire_dept_number=services[Country_name]["fire_dept"]

    # creating label for the Fire department number
    fire_dept_lbl=tk.Label(contacts_frame, text=f"Fire deptpartment: {fire_dept_number}", font="Bold, 12")
    fire_dept_lbl.pack(anchor="w", pady=5)
    
    # PROFILE
    profile_frame=tk.Frame(main_frame, highlightbackground="red", highlightthickness=2, height=560, width=360 )
    profile_frame.pack_propagate(False)
    
    
    def hide_pages():
        for frame in main_frame.winfo_children():
            frame.pack_forget()

    def switch_page(page):
        print(page)
        hide_pages()
        page.pack()
    
    
    #NAVBAR

    #Creating the nav bar
    paddingy=24
    navbar=tk.Frame(root, bg=BACKGROUND, height=40, borderwidth=5, border=5, width=360)
    home_btn=tk.Button(navbar,image=home_icon,bg=BACKGROUND, activebackground=BACKGROUND, relief="flat", bd=0, command=lambda: switch_page(home_frame))
    Checklist_btn=tk.Button(navbar,image=Checklist_icon,bg=BACKGROUND, activebackground=BACKGROUND, relief="flat", bd=0,command=lambda: switch_page(checklist_frame))
    contacts_btn=tk.Button(navbar,image=contacts_icon,bg=BACKGROUND, activebackground=BACKGROUND, relief="flat", bd=0,command=lambda: switch_page(contacts_frame))
    user_btn=tk.Button(navbar,image=user_icon,bg=BACKGROUND, activebackground=BACKGROUND, relief="flat", bd=0, command=lambda: switch_page(profile_frame))

    #packing stuff
    home_btn.pack(side="left", padx=20, pady=paddingy)
    Checklist_btn.pack(side="left", padx=30, pady=paddingy)
    contacts_btn.pack(side="left", padx=30, pady=paddingy)
    user_btn.pack(side="left", padx=30, pady=paddingy)
    navbar.place(x=0,y=560)
    

def getIP()->str:
    """
    Gets Ip dress from the public_ip module

    Returns:
        str: IP adress in string form
    """
    # Python Program to Get IP Address
    
    IPAddr=ip.get()
    return str(IPAddr)

def getcountry(IP:str)->str:
    """
    Finds the country name based on the IP adress entered

    Args:
        IP (str): Public IP adress (IPv4 or IPv6)

    Returns:
        str: Country name
    """
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
        return json_response["officialCountryName"]
    else:
       return 'Failed to retrieve info'
        
def emergency_contacts(Country_name:str)->dict:
    """
    Retrieves emergency contacts from "country.json" based on the country name entered

    Args:
        Country_name (str): A string containing the name of the country program is being ran in

    Returns:
        dict: Dictionary containing the countryas the key, and emergency contacts as the argument
    """
    with open("country_data.json", "r") as file:
        x:dict=json.load(file)
        for country in x["countries"]:
            for place, value in country.items():
                if place==Country_name:
                    country_info={place:value}
                    return country_info

def weather_status():
    pass
    
if __name__=="__main__":
    main()