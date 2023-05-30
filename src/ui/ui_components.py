import customtkinter as ct
from tkinter import PhotoImage, filedialog
from moviepy.editor import AudioFileClip
from load_config import color_stylesheet
from os import getcwd

# Play Button icon by Icons8
class Audio_Tile:
    def __init__(self, root:ct.CTk, x:int, y:int, width:int, height:int, filename:str, index:int) -> None:
        self.audiofile = AudioFileClip(filename)
        filename = filename.split("/" or "\\")[-1]
        self.label = ct.CTkLabel(master=root, width=width, height=height, fg_color="green", text=f"   {filename}")
        self.playbutton = ct.CTkButton(master=root, command=self.play_button, width=25, height=50, image=PhotoImage("/assets/playbutton.png"), hover=True, hover_color="#000000")
        
        #self.add_button = ct.CTkButton()
        #self.del_button = ct.CTkButton()
        
        #self.index = index

        self.x, self.y = x, y
        self.width, self.height = width, height

    def play_button(self) -> None:
        self.audiofile.preview()

    def set_widgets(self, x, y) -> None:
        self.label.place(x=x,y=y)
        self.playbutton.place(x = x, y = y)


class FileOpenButton:
    def __init__(self, root, x:int, y:int, width:int, height:int, llabel) -> None:
        self.root = root
        self.button = ct.CTkButton(master = root, width=width, height=height, command=self.open_file, text="Open file")
        self.llabel = llabel
        self.x, self.y = x, y

    def open_file(self) -> None:
        filepath = filedialog.askopenfilename(initialdir=getcwd(), title="Choose audio file", filetypes=(("MP3 files", "*.mp3"), ("WAVE files", "*.wav")))
        
        new_sound = Audio_Tile(self.root, 0, 0, 180, 50, filepath, 0)
        self.llabel.add_widget(new_sound)

    def set_widgets(self) -> None:
        self.button.place(x = self.x, y = self.y)

class LoadingLabel:
    def __init__(self, root:ct.CTk, x:int, y:int, width:int, height:int, orderbyX:bool) -> None:
        self.loading_label = ct.CTkLabel(master=root, width=width, height=height, fg_color=color_stylesheet.get("widgets"), text="")
        self.loading_label.grid()
        
        self.orderbyX = orderbyX
        
        self.objects_loaded = []

        self.x, self.y = x, y
        self.width, self.height = width, height

    def set_widgets(self):
        self.loading_label.place(x = self.x, y = self.y)

    def add_widget(self, widget:Audio_Tile):
        if len(self.objects_loaded) > 0:
            x, y, h, w = self.objects_loaded[-1].winfo_x(), self.objects_loaded[-1].winfo_y(), self.objects_loaded[-1].height, self.objects_loaded[-1].width
            if self.orderbyX:
                widget.set_widgets(x + w + 10, y)
            else:
                widget.set_widgets(x, y + h + 10)
                
        else:
            x, y = self.x + 15, self.y + 15
            if self.orderbyX:
                widget.set_widgets(x, y + 10)
            else:
                widget.set_widgets(x, y + 10)


    def delete_widget(self, widget):
        self.objects_loaded.remove(widget)

        def sum_all_heights(index):
            s = self.objects_loaded[0].height + 15
            for j in range(1, index + 1):
                s += self.objects_loaded[j].height + 15
            return s
        
        def sum_all_widths(index):
            s = self.objects_loaded[0].width + 15
            for j in range(1, index + 1):
                s += self.objects_loaded[j].width + 15
            return s

        for obj in self.objects_loaded:
            if self.orderbyX:
                obj.set_widgets(self.x + 15, self.y + 15 + sum_all_heights(self.objects_loaded.index(obj)))
            else:
                obj.set_widgets(self.x + 15 + sum_all_widths(self.objects_loaded.index(obj)), self.y + 15)