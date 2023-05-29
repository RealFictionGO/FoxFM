from load_config import get_window
from ui.ui_components import Audio_Tile
import customtkinter as ct

root = get_window()
loading_label = ct.CTkLabel(master=root.root, width=200, height=400, text="Load audio files", fg_color="#FFFFFF")
loading_label.place(x = 10, y = 50)

root.start()