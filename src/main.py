from load_config import get_window
from ui.ui_components import *
import customtkinter as ct

root, color_sheet = get_window(True)

ll = LoadingLabel(root.root, 15, 15, 200, 400, False)
ll.set_widgets()

file_open_button = FileOpenButton(root.root, 15, 425, 200, 50, ll)
file_open_button.set_widgets()

root.start()
