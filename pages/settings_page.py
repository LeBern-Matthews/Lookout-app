from tkinter import Frame, Label, OptionMenu, Radiobutton, Button, StringVar
import backend as bk

class SettingsPage:
    def __init__(self, main_frame, contacts_page, change_theme_callback, change_navbar_theme_callback):
        self.settings_frame = Frame(main_frame, height=560, width=360, 
                                  background=bk.BACKGROUND, name="settings_frame")
        self.settings_frame.pack_propagate(False)
        
        # Location settings
        self.location_frame = Frame(self.settings_frame, background=bk.BACKGROUND, 
                                  name="location_frame")
        self.clicked = StringVar()
        self.clicked.set(bk.text)
        
        def update():
            country_name = self.clicked.get()
            contacts_page.update_contacts(country_name)

        drop = OptionMenu(self.location_frame, self.clicked, *bk.country_options())
        drop.config(bg=bk.NAVBAR_BACKGROUND, activebackground=bk.NAVBAR_BACKGROUND, border=0)
        
        update_btn = Button(self.location_frame, text="Update", command=update,
                          background=bk.NAVBAR_BACKGROUND, activebackground=bk.NAVBAR_BACKGROUND,
                          activeforeground="white", border=3)
        
        location_lbl = Label(self.location_frame, text="Location", font="Bold, 14", 
                           background=bk.BACKGROUND)
        
        # Theme settings
        self.appearance_frame = Frame(self.settings_frame, background=bk.BACKGROUND)
        appearance_lbl = Label(self.appearance_frame, text="Appearance", font="Bold, 14",
                             background=bk.BACKGROUND)
        appearance_lbl_2 = Label(self.appearance_frame, text="Change the theme of the app", 
                               font="Bold, 9", background=bk.BACKGROUND)

        self.theme_var = StringVar(value="light")
        
        def sel():
            if self.theme_var.get() == "light":
                change_theme_callback("black", bk.BACKGROUND)
                change_navbar_theme_callback(bk.NAVBAR_BACKGROUND)
            else:
                change_theme_callback("white", bk.DARKBACKGROUND)
                change_navbar_theme_callback(bk.DARK_NAVBAR_BACKGROUND)

        light_btn = Radiobutton(self.appearance_frame, text="Light", variable=self.theme_var,
                              value="light", command=sel, background=bk.BACKGROUND,
                              activebackground=bk.BACKGROUND)
        dark_btn = Radiobutton(self.appearance_frame, text="Dark", variable=self.theme_var,
                              value="dark", command=sel, background=bk.BACKGROUND,
                              activebackground=bk.BACKGROUND)

        # Packing widgets
        location_lbl.pack(pady=10, padx=5, anchor="w")
        drop.pack(side="left", padx=5)
        update_btn.pack(side="right")
        self.location_frame.place(y=30)

        appearance_lbl.pack(pady=10, padx=5, anchor="w")
        appearance_lbl_2.pack(padx=5, anchor="w")
        light_btn.pack(side="left", padx=5)
        dark_btn.pack(side="left", padx=5)
        self.appearance_frame.place(y=150)