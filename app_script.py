import tkinter as tk
from tkinter import ttk
import public_ip as ip
import requests

root=tk.Tk()
#BACKGROUND="#878672"
BACKGROUND="#545333"
home_icon=tk.PhotoImage(file=r"home.png")
user_icon=tk.PhotoImage(file=r"user.png")
contacts_icon=tk.PhotoImage(file=r"id-card.png")
Checklist_icon=tk.PhotoImage(file=r"test.png")

def main():
    root.title("Lookout")
    root.geometry("360x640")
    #IP=getIP()
    #getcountry(IP)
    layout()
   
    root.resizable(False, False)
    root.mainloop()
    
def layout():
    main_frame=tk.Frame(root, highlightbackground="black", highlightthickness=2) 
    main_frame.pack_propagate(False)
    main_frame.configure(height=560, width=360)
    main_frame.pack(side="top")
    
    
    def home_page():
        home_frame=tk.Frame(main_frame, highlightbackground="black", highlightthickness=2,height=560, width=360)
        
        lb=tk.Label(home_frame, text="home")
        lb.pack()
        
        home_frame.pack()
        
    def checklist_page():
        checklist_frame=tk.Frame(main_frame, highlightbackground="black", highlightthickness=2,height=560, width=360) 
        
        lb=tk.Label(checklist_frame, text="checklist")
        lb.pack()
        
        checklist_frame.pack()
        
        
    def contacts_page():
        contacts_frame=tk.Frame(main_frame, highlightbackground="black", highlightthickness=2,height=560, width=360)
        lb=tk.Label(contacts_frame, text="contacts")
        lb.pack()
        
        contacts_frame.pack()
        
    def profile_page():
        
        profile_frame=tk.Frame(main_frame, highlightbackground="red", highlightthickness=2, height=560, width=360 )
        profile_frame.pack_forget()
        lb=tk.Label(profile_frame, text="profile")
        lb.pack(fill="both")
        
        profile_frame.pack()
    
    def hide_pages():
        for frame in main_frame.winfo_children():
            frame.destroy()
        
    def switch_page(page):

        hide_pages()
        page()
    
    
    
    #Creating the nav bar
    paddingy=24
    navbar=tk.Frame(root, bg=BACKGROUND, height=40, borderwidth=5, border=5, width=360)
    home_btn=tk.Button(navbar,image=home_icon,bg=BACKGROUND, activebackground=BACKGROUND, relief="flat", bd=0, command=lambda: switch_page(home_page))
    Checklist_btn=tk.Button(navbar,image=Checklist_icon,bg=BACKGROUND, activebackground=BACKGROUND, relief="flat", bd=0,command=lambda: switch_page(checklist_page))
    contacts_btn=tk.Button(navbar,image=contacts_icon,bg=BACKGROUND, activebackground=BACKGROUND, relief="flat", bd=0,command=lambda: switch_page(contacts_page))
    user_btn=tk.Button(navbar,image=user_icon,bg=BACKGROUND, activebackground=BACKGROUND, relief="flat", bd=0, command=lambda: switch_page(profile_page))
       
    home_btn.pack(side="left", padx=20, pady=paddingy)
    Checklist_btn.pack(side="left", padx=30, pady=paddingy)
    contacts_btn.pack(side="left", padx=30, pady=paddingy)
    user_btn.pack(side="left", padx=30, pady=paddingy)
    navbar.place(x=0,y=560)
    
    
    

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