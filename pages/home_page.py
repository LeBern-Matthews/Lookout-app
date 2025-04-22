from tkinter import Frame, Label
from tkinter.ttk import Style, Progressbar
import backend as bk

class HomePage:
    def __init__(self, main_frame):
        self.home_frame = Frame(main_frame, height=560, width=360, 
                              background=bk.BACKGROUND, name="home_frame")
        
        # Configure progress bar styles
        new_style = Style()
        new_style.theme_use('alt')
        new_style.configure("Bad.Horizontal.TProgressbar", 
                          background=bk.RED, 
                          troughcolor=bk.BACKGROUND)
        new_style.configure("Moderate.Horizontal.TProgressbar", 
                          background=bk.YELLOW, 
                          troughcolor=bk.BACKGROUND)
        new_style.configure("good.Horizontal.TProgressbar", 
                          background=bk.GREEN, 
                          troughcolor=bk.BACKGROUND)

        # Create preparedness section
        preparedness_meter = Label(self.home_frame, text="Prepared-o-meter", 
                                 font="Bold, 24", background=bk.BACKGROUND)
        self.Progress_bar = Progressbar(self.home_frame, orient="horizontal", 
                                      length=300, mode="determinate", 
                                      style="Bad.Horizontal.TProgressbar")
        self.preparedness_lbl = Label(self.home_frame, text="0%", 
                                    font="Bold, 12", background=bk.BACKGROUND)
        self.encouraged_lbl = Label(self.home_frame, text="You are unprepared for a disaster", 
                                  font="Bold, 12", background=bk.BACKGROUND)
        
        # Create weather section
        weather_frame = Frame(self.home_frame, background=bk.BACKGROUND)
        weather_lbl = Label(weather_frame, font="Bold, 14", text="Weather", 
                          background=bk.BACKGROUND)
        info_lbl = Label(weather_frame, font="underline, 11", text="Last updated at: ", 
                        background=bk.BACKGROUND)
        weather_last_update = Label(weather_frame, font="Bold, 11", 
                                  text=f"{bk.last_updated_msg}", background=bk.BACKGROUND)
        weather_lbl_2 = Label(weather_frame, font="Bold, 12", text=f"{bk.weather}", 
                            background=bk.BACKGROUND)
        weather_description = Label(weather_frame, font="Bold, 12", 
                                  text=f"{bk.description.capitalize()}", background=bk.BACKGROUND)
        weather_temp = Label(weather_frame, font="Bold, 12", text=f"{bk.temp}", 
                           background=bk.BACKGROUND)

        # Pack preparedness section
        preparedness_meter.pack(pady=10)
        self.Progress_bar.pack(padx=0, pady=5)
        self.preparedness_lbl.pack()
        self.encouraged_lbl.pack(pady=5, anchor="w", padx=20)

        # Pack weather section
        weather_lbl.pack(pady=5, anchor="w")
        info_lbl.pack(pady=5, anchor="w")
        weather_last_update.pack(pady=5, anchor="w")
        weather_lbl_2.pack(pady=5, anchor="w")
        weather_description.pack(pady=5, anchor="w")
        weather_temp.pack(pady=5, anchor="w")
        weather_frame.place(y=265, x=20)

        # Configure frame
        self.home_frame.pack_propagate(False)
        self.home_frame.pack()