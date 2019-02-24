import tkinter as tk
from tkinter import Tk, Canvas, Button, messagebox
from PIL import ImageTk, Image
import yaml
from edempresence.edempresence import EdemPresence
from edempresence.edemcard import EdemCard
from edempresence.edemexternalfile import EdemExternalFile
import os

class EdemPresenceGUI():

    config = None

    def __init__(self, parent):

        self.read_config_file()

        self.external_file = EdemExternalFile(filepath=self.configs['save_to_file'])

        edemcard = EdemCard(enrollment='0000')
        self.edempresence = EdemPresence(card=edemcard, external_file=self.external_file)
        filename = self.edempresence.filename()
        self.external_file.filepath=self.configs['save_to_file'] + '/' + filename


        top = self.top = tk.Toplevel(parent)
        self.myEntryBox = tk.Entry(root, width=6)
        self.myEntryBox.config(font=("Courier", 44, 'bold'))
        self.myEntryBox.bind("<Return>", self.show_student_picture)

        self.myEntryBox.focus_set()
        self.myEntryBox.pack()

        Button(root, text="SAIR", command=root.destroy).pack()

    def show_student_picture(self, event):

        self.canvas = Canvas(root, width=400, height=400)

        picture = self.configs['photos_directory'] + '/' + str(self.myEntryBox.get()) + '.jpg'

        print(picture)
        if not os.path.exists(picture):
            picture = os.getcwd() + '/default_picture/default.jpg'

        im = Image.open(picture)
        im = im.resize((400, 400), Image.ANTIALIAS)
        self.canvas.image = ImageTk.PhotoImage(im)
        self.canvas.create_image(0, 0, image=self.canvas.image, anchor='nw')

        self.edempresence.enrollment = str(self.myEntryBox.get())

        data = self.edempresence.generate_full_presence_record()
        self.edempresence.write_external_presence_data(data)

        self.canvas.pack()

        self.myEntryBox.focus_set()
        self.myEntryBox.delete(0, 'end')

    def read_config_file(self):
        with open('edempresence.yaml', 'r') as config:
            self.configs = yaml.load(config)


root = tk.Tk()
root.geometry("600x680")

mf = EdemPresenceGUI(root)

root.mainloop()
