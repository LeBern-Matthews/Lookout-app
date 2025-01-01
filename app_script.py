import tkinter as tk
import socket
from tkinter import ttk
import public_ip as ip
import requests
import json

root=tk.Tk()
#BACKGROUND="#878672"
BACKGROUND="#f4f0dc"
DARKBACKGROUND="#1e1e1e"

NAVBAR_BACKGROUND="#6d6a42"
DARK_NAVBAR_BACKGROUND="#545333"
GREEN="#357C3C"
YELLOW="#FFD700"
RED="#990000"

home_icon=tk.PhotoImage(file=r"home.png")
user_icon=tk.PhotoImage(file=r"setting.png")
contacts_icon=tk.PhotoImage(file=r"id-card.png")
Checklist_icon=tk.PhotoImage(file=r"test.png")

home_icon_white=tk.PhotoImage(file=r"home-white.png")
user_icon_white=tk.PhotoImage(file=r"setting-white.png")
contacts_icon_white=tk.PhotoImage(file=r"id-card-white.png")
Checklist_icon_white=tk.PhotoImage(file=r"test-white.png")

variable_list=[]
essentials=["Water: 1 gallon per person, per day, for at least 3 days", "Non-perishable Food: Canned goods, dries fruits, nuts", "Manual can opener", "First-Aid kit", "Battery-powered or hand-cranked rdio", "Flashlights and extra betteries", "Cell phone charger", "Cash: ATMs may be unavailable", "Important documents: Birth Certificates, insurance policies","Tools", "Hygiene Items", "Wet wipes", "Plastic bags", "work gloves", "Blackets and Pillows", "Rain Gear"]

def main():
    root.title("Lookout")
    root.geometry("360x640")
    
    layout()
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

def layout():
    if has_internet_connection():
        IP=getIP()

        Country_name:str=getcountry(IP)
        text=Country_name
    else:
        Country_name:str="Select a county in settings"
        text:str="Choose location"

    main_frame=tk.Frame(root, name="main_frame") 
    main_frame.pack_propagate(False)
    main_frame.configure(height=560, width=360)
    
    main_frame.pack(side="top")

    def fill_progressbar(check_btn: tk.Checkbutton):
        progresss_fill:int=0
        
        if progresss_fill>=0 and progresss_fill<100:
            for choice in variable_list:
                if choice.get()==1: 
                    progresss_fill+=6.25
                
            if progresss_fill<=33.33:
                Progress_bar.config(style="Bad.Horizontal.TProgressbar")
                encourage_text="unprepared"
            elif progresss_fill<=66.66:
                Progress_bar.config(style="Moderate.Horizontal.TProgressbar")
                encourage_text="sufficiently prepared"
            else:
                Progress_bar.config(style="good.Horizontal.TProgressbar")
                encourage_text="prepared"
            
            percentage=round(progresss_fill, 2)
            preparedness_lbl.config(text=f"{percentage}%")
            encouraged_lbl.config(text=f"You are {encourage_text} for a disaster")
            Progress_bar.configure(value=progresss_fill)
            home_frame.update_idletasks()
        else:
            print("Outside of range")
    
    # HOME PAGE
    home_frame=tk.Frame(main_frame,height=1000, width=360, background=BACKGROUND, name="home_frame")

    new_style=ttk.Style()
    new_style.theme_use('alt')
    new_style.configure("Bad.Horizontal.TProgressbar",background=RED)
    new_style.configure("Moderate.Horizontal.TProgressbar",background=YELLOW)
    new_style.configure("good.Horizontal.TProgressbar",background=GREEN,  foreground=GREEN)

    Progress_bar=ttk.Progressbar(home_frame, orient="horizontal", length=300, mode="determinate", 
                                 style="good.Horizontal.TProgressbar")
    
    preparedness_meter=tk.Label(home_frame, text="Prepared-o-meter", font="Bold, 24", background=BACKGROUND)
    preparedness_lbl=tk.Label(home_frame, text="0%", font="Bold, 12", background=BACKGROUND)
    weather_lbl=tk.Label(home_frame, font="Bold, 12",text="Weather", background=BACKGROUND)
    encouraged_lbl=tk.Label(home_frame, font="Bold, 12", background=BACKGROUND)

    #packing the widgets
    preparedness_meter.pack(pady=10)
    Progress_bar.pack(padx=0, pady=5)
    preparedness_lbl.pack()
    encouraged_lbl.pack(pady=5,anchor="w", padx=20)
    weather_lbl.place(y=265, x=0)
    home_frame.pack_propagate(False)
    home_frame.pack()
    
    # CHECKLIST PAGE
    checklist_frame=tk.Frame(main_frame,height=560, width=360, background=BACKGROUND, name="checklist_frame") 
    checklist_frame.pack_propagate(False)
    
    essential_supplies=tk.Label(checklist_frame, text="Essential supplies", font=("Bold",  16, "underline")
                                , background=BACKGROUND)
    essential_supplies.place(x=0, y=5)
    
    essentials_frame=tk.Frame(checklist_frame, background=BACKGROUND, name="essentials_frame")
    for essential in essentials:
        choiceNum = tk.IntVar()
        check_btn=tk.Checkbutton(essentials_frame, text=f"{essential}", 
                                height=1, variable=choiceNum, command=lambda:fill_progressbar(check_btn)
                                ,bg=BACKGROUND,activebackground=BACKGROUND)
        variable_list.append(choiceNum)
        check_btn.pack_configure(pady=2,anchor="w")
    essentials_frame.place(x=0, y=70)
    
    checklist_frame.pack()

    """
    Creats an emergency contacts page which displays the police, ambulance and fire department contacts
    """
    contacts_frame=tk.Frame(main_frame,height=560, width=360,background=BACKGROUND, name="contacts_frame")
    contacts_frame.pack_propagate(False)
    lb=tk.Label(contacts_frame, text="EMERGENCY CONTACTS", font="Bold, 20", name="contacts"
                ,background=BACKGROUND)
    lb.pack(pady=10)
    def contanct_building(Country_name:str):
        for_country=tk.Label(contacts_frame, text=f"For {Country_name}", font="Bold, 14"
                             , background=BACKGROUND)
        for_country.pack(anchor="w")
        services=emergency_contacts(Country_name)

        # adjsting for multiple numbers
        if type(services[Country_name]["police"])== list:
            police_number=",".join(services[Country_name]["police"])
        else:
            police_number=services[Country_name]["police"]

        # creating label for the Police number
        police_lbl=tk.Label(contacts_frame, text=f"Police: {police_number}", font="Bold, 12"
                            , background=BACKGROUND)
        police_lbl.pack(anchor="w", pady=10)
        
        # adjsting for multiple numbers        
        if type(services[Country_name]["ambulance"])== list:
            ambulance_number=",".join(services[Country_name]["ambulance"])
        else:
            ambulance_number=services[Country_name]["ambulance"]

        # creating label for the Ambulance numbers
        ambulance_lbl=tk.Label(contacts_frame, text=f"Ambulance: {ambulance_number}", font="Bold, 12"
                               , background=BACKGROUND)
        ambulance_lbl.pack(anchor="w", pady=10)

        # adjsting for multiple numbers
        if type(services[Country_name]["fire_dept"])== list:
            fire_dept_number=",".join(services[Country_name]["fire_dept"])
        else:
            fire_dept_number=services[Country_name]["fire_dept"]

        # creating label for the Fire department number
        fire_dept_lbl=tk.Label(contacts_frame, text=f"Fire deptpartment: {fire_dept_number}", font="Bold, 12"
                               , background=BACKGROUND)
        fire_dept_lbl.pack(anchor="w", pady=10)

    contanct_building(Country_name)
    # SETTINGS PAGE
    settings_frame=tk.Frame(main_frame, highlightbackground="red", highlightthickness=2, height=560, width=360
                            , background=BACKGROUND, name="settings_frame") 
    settings_frame.pack_propagate(False)
    
    location_frame=tk.Frame(settings_frame, background=BACKGROUND, name="location_frame")

    def update():

        for widget in contacts_frame.winfo_children():
            if widget.winfo_name()!="contacts":
                widget.destroy()

        Country_name=clicked.get()
        contanct_building(Country_name)

    # Dropdown menu options 
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
    
    # datatype of menu text 
    clicked = tk.StringVar() 
    
    # initial menu text 
    clicked.set(text)
    
    # Create Dropdown menu 
    drop = tk.OptionMenu( location_frame , clicked , *options) 
    drop.config(bg=NAVBAR_BACKGROUND, activebackground=NAVBAR_BACKGROUND
                ,border=0)
    #creating the update button
    update_btn=tk.Button(location_frame, text="Update", command=update
                         , background=NAVBAR_BACKGROUND, activebackground=NAVBAR_BACKGROUND, 
                         activeforeground="white",border=3)

    #creating the label
    location_lbl=tk.Label(location_frame, text="Location", font="Bold, 14", background=BACKGROUND)

    #packing the widgets
    location_lbl.pack(pady=10,padx=5, anchor="w")
    drop.pack(side="left", padx=5) 
    update_btn.pack(side="right")
    location_frame.place(y=30)

    appearance_frame=tk.Frame(settings_frame, background=BACKGROUND)
    appearance_lbl=tk.Label(appearance_frame, text="Appearance", font="Bold, 14"
                            , background=BACKGROUND)
    appearance_lbl_2=tk.Label(appearance_frame, text="Change the theme of the app", font="Bold, 9"
                              , background=BACKGROUND)

    def sel():
        selection = f"You selected the {var.get()} mode"
        if var.get() == "light":
            #changing the nav bar background color
            FORGROUND_COLOR="black"
            change_theme(FORGROUND_COLOR,BACKGROUND)

            root.config(bg=BACKGROUND)

            change_navbar_theme(NAVBAR_BACKGROUND)
        else:
            FORGROUND_COLOR="white"

            change_theme(FORGROUND_COLOR,DARKBACKGROUND )

            #changing the nav background color
            root.config(bg="red")
            change_navbar_theme(DARK_NAVBAR_BACKGROUND)

    var = tk.StringVar(value="light")

    #creating the radio buttons
    light_btn=tk.Radiobutton(appearance_frame, text="Light", variable=var, value="light", command=sel, background=BACKGROUND, activebackground=BACKGROUND)
    dark_btn=tk.Radiobutton(appearance_frame, text="Dark", variable=var, value="dark", command=sel, background=BACKGROUND, activebackground=BACKGROUND)

    #packing the widgets
    appearance_lbl.pack(pady=10,padx=5, anchor="w")
    appearance_lbl_2.pack(padx=5, anchor="w")
    light_btn.pack(side="left", padx=5)
    dark_btn.pack(side="left", padx=5)

    appearance_frame.place(y=150)

    def change_navbar_theme(COLOR:str)->None:
        """
        Changes the color of the nav bar and the buttons in the nav bar to the color passed in the argument

        Parameters:
            COLOR (str): The color to change the nav bar and the buttons in the nav bar to
        """
        navbar.config(bg=COLOR)
        home_btn.config(bg=COLOR, activebackground=COLOR)
        Checklist_btn.config(bg=COLOR, activebackground=COLOR)
        contacts_btn.config(bg=COLOR, activebackground=COLOR)
        user_btn.config(bg=COLOR, activebackground=COLOR)

    def change_theme(FORGROUND_COLOR:str, BACKGROUND_COLOR:str)->None:
        """"
        Changes the colour for the widgets in the frame "main_frame" to match the color passed in the argument

        Parameters:
            FORGROUND_COLOR (str): The color of the text in the widgets
            BACKGROUND_COLOR (str): The background color of the widgets
        """
        drop.config(highlightcolor=FORGROUND_COLOR)
        for page in main_frame.winfo_children():
            page.config(bg=BACKGROUND_COLOR)
            for children in page.winfo_children():
                if type(children)==tk.Frame:
                    children.config(bg=BACKGROUND_COLOR)

                    for widget in children.winfo_children():
                        widget.config(fg=FORGROUND_COLOR)
                        widget.config(bg=BACKGROUND_COLOR)
                        if children.winfo_name()=="location_frame" and type(widget)==tk.Button:
                            widget.config(highlightcolor=FORGROUND_COLOR,highlightbackground = FORGROUND_COLOR)

                        if type(widget)==tk.Checkbutton:
                            widget.config(selectcolor=BACKGROUND_COLOR
                            ,activebackground=BACKGROUND_COLOR)
                     

                elif type(children)==tk.Label:
                    children.config(fg=FORGROUND_COLOR)
                    children.config(bg=BACKGROUND_COLOR)
  
    def hide_pages():
        """
        Hides all the pages in the frame "main_frame"
        """
        for frame in main_frame.winfo_children():
            frame.pack_forget()

    def switch_page(page:tk.Frame):
        """
        Switches to the frame clicked 

        Args:
            page(Frame): tkinter frame relating to the page 
        """
        home_btn.config(image=home_icon)
        Checklist_btn.config(image=Checklist_icon)
        contacts_btn.config(image=contacts_icon)
        user_btn.config(image=user_icon)

        match page.winfo_name():
            case "home_frame":
                home_btn.config(image=home_icon_white)
            case "checklist_frame":
                Checklist_btn.config(image=Checklist_icon_white)
            case "contacts_frame":
                contacts_btn.config(image=contacts_icon_white)
            case "settings_frame":
                user_btn.config(image=user_icon_white)
            case _:
                pass
        hide_pages()
        page.pack()
    
    #NAVBAR
    #Creating the nav bar
    paddingy=24
    navbar=tk.Frame(root, bg=NAVBAR_BACKGROUND, height=40, borderwidth=5, border=5, width=360)
    home_btn=tk.Button(navbar,image=home_icon,bg=NAVBAR_BACKGROUND, activebackground=NAVBAR_BACKGROUND, relief="flat", bd=0, command=lambda: switch_page(home_frame))
    Checklist_btn=tk.Button(navbar,image=Checklist_icon,bg=NAVBAR_BACKGROUND, activebackground=NAVBAR_BACKGROUND, relief="flat", bd=0,command=lambda: switch_page(checklist_frame))
    contacts_btn=tk.Button(navbar,image=contacts_icon,bg=NAVBAR_BACKGROUND, activebackground=NAVBAR_BACKGROUND, relief="flat", bd=0,command=lambda: switch_page(contacts_frame))
    user_btn=tk.Button(navbar,image=user_icon,bg=NAVBAR_BACKGROUND, activebackground=NAVBAR_BACKGROUND, relief="flat", bd=0, command=lambda: switch_page(settings_frame))

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
        IP (str): Public IP address (IPv4 or IPv6)

    Returns:
        str: Country name
    """
    # Define API URL
    BASE_URL = 'https://apiip.net/api/check?ip='
    
    API_URL=BASE_URL+IP+'&accessKey=d4f9b109-0a44-4e29-8cdc-c66c07de1942'
   
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

def has_internet_connection()->bool:
    """
    Checks if the device has an active internet connection.
    
    Returns:
        bool: True if connected to the internet, False otherwise.
    """
    try:
        # Try connecting to a public domain (like google.com)
        socket.create_connection(("8.8.8.8", 53)) 
        return True
    except Exception:
        return False

def weather_status():
    pass
    
if __name__=="__main__":
    main()