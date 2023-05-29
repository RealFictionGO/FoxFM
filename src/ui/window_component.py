import customtkinter as ct

class Window_Component:
    def __init__(self, appearance:str, color_theme:str) -> None:    
        ct.set_appearance_mode(appearance)
        ct.set_default_color_theme(color_theme)

        self.root = ct.CTk()
        self.root.geometry("800x500")

    def start(self) -> None:
        self.root.mainloop()