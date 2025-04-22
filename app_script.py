from tkinter import Frame, Label, Button, Checkbutton
import backend as bk
from pages.home_page import HomePage
from pages.checklist_page import ChecklistPage
from pages.emergency_contacts import EmergencyContactsPage
from pages.settings_page import SettingsPage

# Initialize root and variables
variable_list = []

def main():
    """Main function that runs the program"""
    bk.root.title("Lookout")
    bk.root.geometry("360x640")
    bk.root.resizable(False, False)
    bk.root.iconphoto(False, bk.root_image)
    
    layout()
    center_window(bk.root)
    bk.root.mainloop()

def center_window(window):
    """Centers the window on the screen"""
    window.update_idletasks()
    width = window.winfo_width()
    height = window.winfo_height()
    x = (window.winfo_screenwidth() - width) // 2
    y = (window.winfo_screenheight() - height) // 2
    window.geometry(f"{width}x{height}+{x}+{y}")

def create_navbar(main_frame, home_page, checklist_page, contacts_page, settings_page, switch_page):
    """Creates and returns the navigation bar"""
    navbar = Frame(bk.root, bg=bk.NAVBAR_BACKGROUND, height=40, 
                  borderwidth=5, border=5, width=360)
    
    buttons = [
        (home_btn := Button(navbar, image=bk.home_icon_white, command=lambda: switch_page(home_page.home_frame))),
        (checklist_btn := Button(navbar, image=bk.checklist_icon, command=lambda: switch_page(checklist_page.checklist_frame))),
        (contacts_btn := Button(navbar, image=bk.contacts_icon, command=lambda: switch_page(contacts_page.contacts_frame))),
        (user_btn := Button(navbar, image=bk.user_icon, command=lambda: switch_page(settings_page.settings_frame)))
    ]
    
    # Configure all buttons
    for btn in buttons:
        btn.config(bg=bk.NAVBAR_BACKGROUND, activebackground=bk.NAVBAR_BACKGROUND, 
                  relief="flat", bd=0)
    
    # Pack buttons
    home_btn.pack(side="left", padx=20, pady=24)
    checklist_btn.pack(side="left", padx=30, pady=24)
    contacts_btn.pack(side="left", padx=30, pady=24)
    user_btn.pack(side="left", padx=30, pady=24)
    
    navbar.place(x=0, y=560)
    return navbar, home_btn, checklist_btn, contacts_btn, user_btn

def layout():
    """Creates the layout of the app"""
    bk.weather_stuff()     
    main_frame = Frame(bk.root, name="main_frame") 
    main_frame.pack_propagate(False)
    main_frame.configure(height=560, width=360)
    main_frame.pack(side="top")

    def change_theme(foreground_color: str, background_color: str) -> None:
        """Changes the color theme of all widgets"""
        for page in main_frame.winfo_children():
            page.config(bg=background_color)
            for child in page.winfo_children():
                if isinstance(child, Frame):
                    child.config(bg=background_color)
                    for widget in child.winfo_children():
                        widget.config(fg=foreground_color, bg=background_color)
                        if child.winfo_name() == "location_frame" and isinstance(widget, Button):
                            widget.config(highlightcolor=foreground_color, 
                                       highlightbackground=foreground_color)
                        if isinstance(widget, Checkbutton):
                            widget.config(selectcolor=background_color,
                                       activebackground=background_color)
                elif isinstance(child, Label):
                    child.config(fg=foreground_color, bg=background_color)

    def change_navbar_theme(color: str) -> None:
        """Changes the navbar color theme"""
        navbar.config(bg=color)
        for btn in [home_btn, checklist_btn, contacts_btn, user_btn]:
            btn.config(bg=color, activebackground=color)

    def switch_page(page: Frame) -> None:
        """Switches to the selected page"""
        # Reset all button images
        button_configs = {
            home_btn: bk.home_icon,
            checklist_btn: bk.checklist_icon,
            contacts_btn: bk.contacts_icon,
            user_btn: bk.user_icon
        }
        
        for btn, icon in button_configs.items():
            btn.config(image=icon)
            
        # Set active button image
        frame_to_button = {
            "home_frame": (home_btn, bk.home_icon_white),
            "checklist_frame": (checklist_btn, bk.checklist_icon_white),
            "contacts_frame": (contacts_btn, bk.contacts_icon_white),
            "settings_frame": (user_btn, bk.user_icon_white)
        }
        
        if page.winfo_name() in frame_to_button:
            button, icon = frame_to_button[page.winfo_name()]
            button.config(image=icon)
            
        # Switch pages
        for frame in main_frame.winfo_children():
            frame.pack_forget()
        page.pack()

    def fill_progressbar(check_btn: Checkbutton) -> None:
        """Updates the progress bar based on checked items"""
        if not variable_list:
            return
            
        checked_count = sum(var.get() for var in variable_list)
        progress_fill = (checked_count * 100.0) / len(variable_list)
        
        # Update progress bar appearance and text
        if progress_fill <= 33.33:
            style, status = "Bad.Horizontal.TProgressbar", "unprepared"
        elif progress_fill <= 66.66:
            style, status = "Moderate.Horizontal.TProgressbar", "sufficiently prepared"
        else:
            style, status = "good.Horizontal.TProgressbar", "prepared"
        
        percentage = round(progress_fill, 2)
        home_page.Progress_bar.config(style=style, value=progress_fill)
        home_page.preparedness_lbl.config(text=f"{percentage}%")
        home_page.encouraged_lbl.config(text=f"You are {status} for a disaster")
        home_page.home_frame.update_idletasks()
    
    # Initialize pages
    home_page = HomePage(main_frame)
    checklist_page = ChecklistPage(main_frame, variable_list, fill_progressbar)
    contacts_page = EmergencyContactsPage(main_frame)
    settings_page = SettingsPage(main_frame, contacts_page, change_theme, change_navbar_theme)

    # Create navbar and get button references
    navbar, home_btn, checklist_btn, contacts_btn, user_btn = create_navbar(
        main_frame, home_page, checklist_page, contacts_page, settings_page, switch_page
    )

if __name__ == "__main__":
    main()