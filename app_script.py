#import tkinter as tk
from tkinter import Frame, Label, OptionMenu, Radiobutton, Button, Checkbutton, StringVar, IntVar
from tkinter.ttk import Style, Progressbar
import backend as bk
from pages.home_page import HomePage
from pages.checklist_page import ChecklistPage
from pages.emergency_contacts import EmergencyContactsPage
from pages.settings_page import SettingsPage

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
    main_frame = Frame(bk.root, name="main_frame") 
    main_frame.pack_propagate(False)
    main_frame.configure(height=560, width=360)
    main_frame.pack(side="top")

    def change_theme(FORGROUND_COLOR:str, BACKGROUND_COLOR:str)->None:
        """"
        Changes the colour for the widgets in the frame "main_frame" to match the color passed in the argument

        Parameters:
            FORGROUND_COLOR (str): The color of the text in the widgets
            BACKGROUND_COLOR (str): The background color of the widgets
        """
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

    def fill_progressbar(check_btn: Checkbutton):
        """
        Updates the progress bar based on checked items
        """
        progresss_fill = 0
        
        # Calculate total progress from all checkboxes
        if len(variable_list) > 0:  # Prevent division by zero
            for choice in variable_list:
                if choice.get() == 1:
                    progresss_fill += (100.0 / len(variable_list))
            
            # Update progress bar appearance and text
            if progresss_fill <= 33.33:
                home_page.Progress_bar.config(style="Bad.Horizontal.TProgressbar")
                encourage_text = "unprepared"
            elif progresss_fill <= 66.66:
                home_page.Progress_bar.config(style="Moderate.Horizontal.TProgressbar")
                encourage_text = "sufficiently prepared"
            else:
                home_page.Progress_bar.config(style="good.Horizontal.TProgressbar")
                encourage_text = "prepared"
            
            percentage = round(progresss_fill, 2)
            home_page.preparedness_lbl.config(text=f"{percentage}%")
            home_page.encouraged_lbl.config(text=f"You are {encourage_text} for a disaster")
            home_page.Progress_bar.configure(value=progresss_fill)
            home_page.home_frame.update_idletasks()
    
    # Initialize pages
    home_page = HomePage(main_frame)
    checklist_page = ChecklistPage(main_frame, variable_list, fill_progressbar)
    contacts_page = EmergencyContactsPage(main_frame)
    settings_page = SettingsPage(main_frame, contacts_page, change_theme, change_navbar_theme)

    # Create navbar
    paddingy=24
    navbar = Frame(bk.root, bg=bk.NAVBAR_BACKGROUND, height=40, borderwidth=5, border=5, width=360)
    Checklist_btn=Button(navbar,image=bk.checklist_icon,bg=bk.NAVBAR_BACKGROUND, 
                        activebackground=bk.NAVBAR_BACKGROUND, relief="flat", bd=0,
                        command=lambda: switch_page(checklist_page.checklist_frame))
    contacts_btn=Button(navbar,image=bk.contacts_icon,bg=bk.NAVBAR_BACKGROUND, 
                       activebackground=bk.NAVBAR_BACKGROUND, relief="flat", bd=0,
                       command=lambda: switch_page(contacts_page.contacts_frame))
    user_btn=Button(navbar,image=bk.user_icon,bg=bk.NAVBAR_BACKGROUND, 
                   activebackground=bk.NAVBAR_BACKGROUND, relief="flat", bd=0, 
                   command=lambda: switch_page(settings_page.settings_frame))
    home_btn=Button(navbar,image=bk.home_icon_white,bg=bk.NAVBAR_BACKGROUND, 
                   activebackground=bk.NAVBAR_BACKGROUND, relief="flat", bd=0, 
                   command=lambda: switch_page(home_page.home_frame))

    #packing stuff
    home_btn.pack(side="left", padx=20, pady=paddingy)
    Checklist_btn.pack(side="left", padx=30, pady=paddingy)
    contacts_btn.pack(side="left", padx=30, pady=paddingy)
    user_btn.pack(side="left", padx=30, pady=paddingy)
    navbar.place(x=0,y=560)

    def switch_page(page: Frame):
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
        for frame in main_frame.winfo_children():
            frame.pack_forget()
        page.pack()
  
if __name__=="__main__":
    main()