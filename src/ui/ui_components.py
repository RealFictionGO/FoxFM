import customtkinter as ct
from tkinter import PhotoImage
from moviepy.editor import AudioFileClip

# Play Button icon by Icons8
class Audio_Tile:
    def __init__(self, root:ct.CTk, width:int, height:int, filename:str) -> None:
        self.audiofile = AudioFileClip(filename)
        self.label = ct.CTkLabel(root.root, width=width, height=height, fg_color="green")
        self.playbutton = ct.CTkButton(root.root, command=self.play_button, width=50, height=50, image=PhotoImage("/assets/playbutton.png"), hover=True, hover_color="light_color")
    
    def play_button(self) -> None:
        self.audiofile.preview()
