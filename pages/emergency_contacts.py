from tkinter import Frame, Label
import backend as bk

class EmergencyContactsPage:
    def __init__(self, main_frame):
        self.contacts_frame = Frame(main_frame, height=560, width=360, 
                                  background=bk.BACKGROUND, name="contacts_frame")
        self.contacts_frame.pack_propagate(False)
        self.title_label = Label(self.contacts_frame, text="EMERGENCY CONTACTS", 
                                font="Bold, 20", name="contacts", background=bk.BACKGROUND)
        self.title_label.pack(pady=10)
        self.update_contacts(bk.Country_name)
        
    def update_contacts(self, country_name: str):
        for widget in self.contacts_frame.winfo_children():
            if widget.winfo_name() != "contacts":
                widget.destroy()

        for_country = Label(self.contacts_frame, text=f"For {country_name}", 
                          font="Bold, 14", background=bk.BACKGROUND)
        for_country.pack(anchor="w")
        services = bk.emergency_contacts(country_name)

        # Handle police numbers
        police_number = ",".join(services[country_name]["police"]) if isinstance(services[country_name]["police"], list) else services[country_name]["police"]
        police_lbl = Label(self.contacts_frame, text=f"Police: {police_number}", 
                          font="Bold, 12", background=bk.BACKGROUND)
        police_lbl.pack(anchor="w", pady=10)
        
        # Handle ambulance numbers
        ambulance_number = ",".join(services[country_name]["ambulance"]) if isinstance(services[country_name]["ambulance"], list) else services[country_name]["ambulance"]
        ambulance_lbl = Label(self.contacts_frame, text=f"Ambulance: {ambulance_number}", 
                            font="Bold, 12", background=bk.BACKGROUND)
        ambulance_lbl.pack(anchor="w", pady=10)

        # Handle fire department numbers
        fire_dept_number = ",".join(services[country_name]["fire_dept"]) if isinstance(services[country_name]["fire_dept"], list) else services[country_name]["fire_dept"]
        fire_dept_lbl = Label(self.contacts_frame, text=f"Fire department: {fire_dept_number}", 
                            font="Bold, 12", background=bk.BACKGROUND)
        fire_dept_lbl.pack(anchor="w", pady=10)