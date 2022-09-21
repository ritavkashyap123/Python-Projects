from tkinter import *
from PIL import Image, ImageTk
from tkinter import filedialog
import object_detection as object_detection
import imagio
import cv2
class window(Frame):
    def __init__(self, master=None):
        Frame.__init_(self, master)
        self.master = master
        self.pos = []
        self.line = []
        self.rect = []
        self.master.title("GUI")
        self.pack(fill=BOTH, example=1)
        self.counter=0
        menu=menu(self.master)
        self.master.config(menu=menu)
        file=Menu(menu)
        file.add_command(label="Open", command=self.open_file)
        file.add_command(label="Exit", command=self.client_exit)
        menu.add_cascade(label="File", menu=file)
        analyze=Menu(menu)
        analyze.add_command(label="Region of Interest", command=self.regionOfInterest)
        menu.add_cascade(label="Analyze", menu=analyze)