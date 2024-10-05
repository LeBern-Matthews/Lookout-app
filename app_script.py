import tkinter as tk

#main app class

class LookOutApp():
    def __init__(self, root) -> None:
        self.root=root
        self.root.geography="500X500"
        self.root.title=""
        


root=tk.Tk()
App=LookOutApp(root)
root.mainloop()