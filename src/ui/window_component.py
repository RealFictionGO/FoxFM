import customtkinter as ct

class Window_Component:
    def __init__(self, appearance:str, color_theme:str) -> None:    
        ct.set_appearance_mode(appearance)
        ct.set_default_color_theme(color_theme)

        self.root = ct.CTk()
        self.root.geometry("800x500")

        self.component_list = []

    def pack_components(self):
        for component in self.component_list:
            component.pack()

    def start(self) -> None:
        self.pack_components()
        self.root.mainloop()