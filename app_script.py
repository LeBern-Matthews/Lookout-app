#import tkinter as tk
from tkinter import Frame, Label, OptionMenu, Radiobutton, Button, Checkbutton, StringVar, IntVar
from tkinter.ttk import Style, Progressbar
import backend as bk

bk.root

variable_list=[]

def main():
    """
    # Main function that runs the program
    """
    bk.root.title("Lookout")
    bk.root.geometry("360x640")
    
    layout()
    bk.root.resizable(False, False)
    center_window(bk.root)
    bk.root.iconphoto(False, bk.root_image)
    bk.root.mainloop()

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
    """
    Creates the layout of the app
    """
    bk.weather_stuff()     
    main_frame=Frame(bk.root, name="main_frame") 
    main_frame.pack_propagate(False)
    main_frame.configure(height=560, width=360)
    
    main_frame.pack(side="top")

    def fill_progressbar(check_btn: Checkbutton):
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
    home_frame=Frame(main_frame,height=1000, width=360, background=bk.BACKGROUND, name="home_frame")

    new_style=Style()
    new_style.theme_use('alt')
    new_style.configure("Bad.Horizontal.TProgressbar",background=bk.RED)
    new_style.configure("Moderate.Horizontal.TProgressbar",background=bk.YELLOW)
    new_style.configure("good.Horizontal.TProgressbar",background=bk.GREEN,  foreground=bk.GREEN)

    Progress_bar=Progressbar(home_frame, orient="horizontal", length=300, mode="determinate", 
                                 style="good.Horizontal.TProgressbar")
    
    preparedness_meter=Label(home_frame, text="Prepared-o-meter", font="Bold, 24", background=bk.BACKGROUND)
    preparedness_lbl=Label(home_frame, text="0%", font="Bold, 12", background=bk.BACKGROUND)

    weather_frame=Frame(home_frame, background=bk.BACKGROUND)
    encouraged_lbl=Label(home_frame, font="Bold, 12", background=bk.BACKGROUND)

    weather_lbl=Label(weather_frame, font="Bold, 14",text="Weather", background=bk.BACKGROUND)
    
    weather_lbl_2=Label(weather_frame, font="Bold, 12", text=f"{bk.weather}", background=bk.BACKGROUND)
    weather_description=Label(weather_frame, font="Bold, 12", text=f"{bk.description.capitalize()}", background=bk.BACKGROUND)
    weather_temp=Label(weather_frame, font="Bold, 12", text=f"{bk.temp}", background=bk.BACKGROUND)
    info_lbl=Label(weather_frame, font="underline, 11", text=f"Last updated at: ", background=bk.BACKGROUND)
    weather_last_update=Label(weather_frame, font="Bold, 11", text=f"{bk.last_updated_msg}", background=bk.BACKGROUND)

    #packing the widgets
    preparedness_meter.pack(pady=10)
    Progress_bar.pack(padx=0, pady=5)
    preparedness_lbl.pack()
    encouraged_lbl.pack(pady=5,anchor="w", padx=20)

    #packing the widgets for the weather
    weather_lbl.pack(pady=5,anchor="w")
    info_lbl.pack(pady=5,anchor="w")
    weather_last_update.pack(pady=5,anchor="w")
    weather_lbl_2.pack(pady=5,anchor="w")
    weather_description.pack(pady=5,anchor="w")
    weather_temp.pack(pady=5,anchor="w")
    weather_frame.place(y=265, x=20)

    #packing the widgets for the home frame
    home_frame.pack_propagate(False)
    home_frame.pack()
    
    # CHECKLIST PAGE
    checklist_frame=Frame(main_frame,height=560, width=360, background=bk.BACKGROUND, name="checklist_frame") 
    checklist_frame.pack_propagate(False)
    
    essential_supplies=Label(checklist_frame, text="Essential supplies", font=("Bold",  16, "underline")
                                , background=bk.BACKGROUND)
    essential_supplies.place(x=0, y=5)
    
    essentials_frame=Frame(checklist_frame, background=bk.BACKGROUND, name="essentials_frame")
    for essential in bk.get_essentials():
        choiceNum = IntVar()
        check_btn=Checkbutton(essentials_frame, text=f"{essential}", 
                                height=1, variable=choiceNum, command=lambda:fill_progressbar(check_btn)
                                ,bg=bk.BACKGROUND,activebackground=bk.BACKGROUND)
        variable_list.append(choiceNum)
        check_btn.pack_configure(pady=2,anchor="w")
    essentials_frame.place(x=0, y=70)
    
    checklist_frame.pack()

    """
    Creats an emergency contacts page which displays the police, ambulance and fire department contacts
    """
    contacts_frame=Frame(main_frame,height=560, width=360,background=bk.BACKGROUND, name="contacts_frame")
    contacts_frame.pack_propagate(False)
    lb=Label(contacts_frame, text="EMERGENCY CONTACTS", font="Bold, 20", name="contacts"
                ,background=bk.BACKGROUND)
    lb.pack(pady=10)
    def contanct_building(Country_name:str):
        for_country=Label(contacts_frame, text=f"For {Country_name}", font="Bold, 14"
                             , background=bk.BACKGROUND)
        for_country.pack(anchor="w")
        services=bk.emergency_contacts(Country_name)

        # adjsting for multiple numbers
        if type(services[Country_name]["police"])== list:
            police_number=",".join(services[Country_name]["police"])
        else:
            police_number=services[Country_name]["police"]

        # creating label for the Police number
        police_lbl=Label(contacts_frame, text=f"Police: {police_number}", font="Bold, 12"
                            , background=bk.BACKGROUND)
        police_lbl.pack(anchor="w", pady=10)
        
        # adjsting for multiple numbers        
        if type(services[Country_name]["ambulance"])== list:
            ambulance_number=",".join(services[Country_name]["ambulance"])
        else:
            ambulance_number=services[Country_name]["ambulance"]

        # creating label for the Ambulance numbers
        ambulance_lbl=Label(contacts_frame, text=f"Ambulance: {ambulance_number}", font="Bold, 12"
                               , background=bk.BACKGROUND)
        ambulance_lbl.pack(anchor="w", pady=10)

        # adjsting for multiple numbers
        if type(services[Country_name]["fire_dept"])== list:
            fire_dept_number=",".join(services[Country_name]["fire_dept"])
        else:
            fire_dept_number=services[Country_name]["fire_dept"]

        # creating label for the Fire department number
        fire_dept_lbl=Label(contacts_frame, text=f"Fire deptpartment: {fire_dept_number}", font="Bold, 12"
                               , background=bk.BACKGROUND)
        fire_dept_lbl.pack(anchor="w", pady=10)

    contanct_building(bk.Country_name)
    # SETTINGS PAGE
    settings_frame=Frame(main_frame, height=560, width=360
                            , background=bk.BACKGROUND, name="settings_frame") 
    settings_frame.pack_propagate(False)
    
    location_frame=Frame(settings_frame, background=bk.BACKGROUND, name="location_frame")

    def update():

        for widget in contacts_frame.winfo_children():
            if widget.winfo_name()!="contacts":
                widget.destroy()

        Country_name=clicked.get()
        contanct_building(Country_name)

    # datatype of menu text 
    clicked = StringVar() 
    
    # initial menu text 
    clicked.set(bk.text)
    
    # Create Dropdown menu 
    drop = OptionMenu( location_frame , clicked , *bk.country_options()) 
    drop.config(bg=bk.NAVBAR_BACKGROUND, activebackground=bk.NAVBAR_BACKGROUND
                ,border=0)
    #creating the update button
    update_btn=Button(location_frame, text="Update", command=update
                         , background=bk.NAVBAR_BACKGROUND, activebackground=bk.NAVBAR_BACKGROUND, 
                         activeforeground="white",border=3)

    #creating the label
    location_lbl=Label(location_frame, text="Location", font="Bold, 14", background=bk.BACKGROUND)

    #packing the widgets
    location_lbl.pack(pady=10,padx=5, anchor="w")
    drop.pack(side="left", padx=5) 
    update_btn.pack(side="right")
    location_frame.place(y=30)

    appearance_frame=Frame(settings_frame, background=bk.BACKGROUND)
    appearance_lbl=Label(appearance_frame, text="Appearance", font="Bold, 14"
                            , background=bk.BACKGROUND)
    appearance_lbl_2=Label(appearance_frame, text="Change the theme of the app", font="Bold, 9"
                              , background=bk.BACKGROUND)

    def sel():
        selection = f"You selected the {var.get()} mode"
        if var.get() == "light":
            #changing the nav bar background color
            FORGROUND_COLOR="black"
            change_theme(FORGROUND_COLOR,bk.BACKGROUND)

            bk.root.config(bg=bk.BACKGROUND)

            change_navbar_theme(bk.NAVBAR_BACKGROUND)
        else:
            FORGROUND_COLOR="white"
            change_theme(FORGROUND_COLOR,bk.DARKBACKGROUND )

            #changing the nav background color
            change_navbar_theme(bk.DARK_NAVBAR_BACKGROUND)

    var = StringVar(value="light")

    #creating the radio buttons
    light_btn=Radiobutton(appearance_frame, text="Light", variable=var, value="light", command=sel, background=bk.BACKGROUND, activebackground=bk.BACKGROUND)
    dark_btn=Radiobutton(appearance_frame, text="Dark", variable=var, value="dark", command=sel, background=bk.BACKGROUND, activebackground=bk.BACKGROUND)

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
                if type(children)==Frame:
                    children.config(bg=BACKGROUND_COLOR)

                    for widget in children.winfo_children():
                        widget.config(fg=FORGROUND_COLOR)
                        widget.config(bg=BACKGROUND_COLOR)
                        if children.winfo_name()=="location_frame" and type(widget)==Button:
                            widget.config(highlightcolor=FORGROUND_COLOR,highlightbackground = FORGROUND_COLOR)

                        if type(widget)==Checkbutton:
                            widget.config(selectcolor=BACKGROUND_COLOR
                            ,activebackground=BACKGROUND_COLOR)
                     

                elif type(children)==Label:
                    children.config(fg=FORGROUND_COLOR)
                    children.config(bg=BACKGROUND_COLOR)
  
    def hide_pages():
        """
        Hides all the pages in the frame "main_frame"
        """
        for frame in main_frame.winfo_children():
            frame.pack_forget()

    def switch_page(page:Frame):
        """
        Switches to the frame clicked 

        Args:
            page(Frame): tkinter frame relating to the page 
        """
        home_btn.config(image=bk.home_icon)
        Checklist_btn.config(image=bk.checklist_icon)
        contacts_btn.config(image=bk.contacts_icon)
        user_btn.config(image=bk.user_icon)

        match page.winfo_name():
            case "home_frame":
                home_btn.config(image=bk.home_icon_white)
            case "checklist_frame":
                Checklist_btn.config(image=bk.checklist_icon_white)
            case "contacts_frame":
                contacts_btn.config(image=bk.contacts_icon_white)
            case "settings_frame":
                user_btn.config(image=bk.user_icon_white)
            case _:
                pass
        hide_pages()
        page.pack()
    
    #NAVBAR
    #Creating the nav bar
    paddingy=24
    navbar=Frame(bk.root, bg=bk.NAVBAR_BACKGROUND, height=40, borderwidth=5, border=5, width=360)
    Checklist_btn=Button(navbar,image=bk.checklist_icon,bg=bk.NAVBAR_BACKGROUND, activebackground=bk.NAVBAR_BACKGROUND, relief="flat", bd=0,command=lambda: switch_page(checklist_frame))
    contacts_btn=Button(navbar,image=bk.contacts_icon,bg=bk.NAVBAR_BACKGROUND, activebackground=bk.NAVBAR_BACKGROUND, relief="flat", bd=0,command=lambda: switch_page(contacts_frame))
    user_btn=Button(navbar,image=bk.user_icon,bg=bk.NAVBAR_BACKGROUND, activebackground=bk.NAVBAR_BACKGROUND, relief="flat", bd=0, command=lambda: switch_page(settings_frame))
    home_btn=Button(navbar,image=bk.home_icon_white,bg=bk.NAVBAR_BACKGROUND, activebackground=bk.NAVBAR_BACKGROUND, relief="flat", bd=0, command=lambda: switch_page(home_frame))

    #packing stuff
    home_btn.pack(side="left", padx=20, pady=paddingy)
    Checklist_btn.pack(side="left", padx=30, pady=paddingy)
    contacts_btn.pack(side="left", padx=30, pady=paddingy)
    user_btn.pack(side="left", padx=30, pady=paddingy)
    navbar.place(x=0,y=560)

if __name__=="__main__":
    main()