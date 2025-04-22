from tkinter import Frame, Label, Checkbutton, IntVar
import backend as bk

class ChecklistPage:
    def __init__(self, main_frame, variable_list, fill_progressbar):
        self.checklist_frame = Frame(main_frame, height=560, width=360, 
                                   background=bk.BACKGROUND, name="checklist_frame")
        self.checklist_frame.pack_propagate(False)
        
        essential_supplies = Label(self.checklist_frame, text="Essential supplies", 
                                 font=("Bold", 16, "underline"), background=bk.BACKGROUND)
        essential_supplies.place(x=0, y=5)
        
        essentials_frame = Frame(self.checklist_frame, background=bk.BACKGROUND, 
                               name="essentials_frame")
        for essential in bk.get_essentials():
            choiceNum = IntVar()
            check_btn = Checkbutton(essentials_frame, text=f"{essential}", height=1, 
                                  variable=choiceNum, command=lambda:fill_progressbar(check_btn),
                                  bg=bk.BACKGROUND, activebackground=bk.BACKGROUND)
            variable_list.append(choiceNum)
            check_btn.pack_configure(pady=2, anchor="w")
        essentials_frame.place(x=0, y=70)
        
        self.checklist_frame.pack()