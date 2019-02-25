import tkinter as tk
from tkinter import Tk, Canvas, Button, messagebox
from PIL import ImageTk, Image
import yaml
from edempresence.edempresence import EdemPresence
from edempresence.edemcard import EdemCard
from edempresence.edemexternalfile import EdemExternalFile
import os
import glob

class EdemPresenceGUI():

    config = None

    def __init__(self, parent):

        self.read_config_file()

        self.external_file = EdemExternalFile(filepath=self.configs['save_to_file'])

        self.photos = self.load_photos(file_path=self.configs['photos_directory'])

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

        self.canvas = Canvas(root, width=300, height=400)

    def load_photos(self, file_path):

        db_fotos = {}                                                                                      
                                                           
        files = glob.glob(file_path + "/*")                                                                
                                                           
        for f in files:                                                                                    
            file_name = os.path.basename(f)                                                                
                                                           
            records = file_name.split('_')                                                                 
            last = records[-1:]                                                                            
                                                           
            mean_parts = last[0].split('.')                                                                
            enrollment = mean_parts[0]                                                                     
                                                           
            if len(enrollment) == 4:                                                                       
                enrollment = '00' + str(enrollment)                                                        
                                                           
            if len(enrollment) == 5:                                                                       
                enrollment = '0' + str(enrollment)                                                         
                                                           
            db_fotos[str(enrollment)] = f                                                                  
                                                           
        return db_fotos   

    def show_student_picture(self, event):

        if self.canvas:
            self.canvas.delete("all")

        self.canvas = Canvas(root, width=300, height=400)
        
        if str(self.myEntryBox.get()) in self.photos.keys():
            picture = self.photos[str(self.myEntryBox.get())]
            print(self.photos[str(self.myEntryBox.get())])
        else:
            picture = os.getcwd() + '/default_picture/default.jpg'

        if not os.path.exists(picture):
            picture = os.getcwd() + '/default_picture/default.jpg'
 
        print("FOTO DO ALUNO: " + str(picture) )
        im = Image.open(picture)
        im = im.resize((300, 400), Image.ANTIALIAS)
        self.canvas.image = ImageTk.PhotoImage(im)
        self.canvas.create_image(0, 0, image=self.canvas.image, anchor='nw')

        self.edempresence.enrollment = str(self.myEntryBox.get())

        data = self.edempresence.generate_full_presence_record()
        self.edempresence.write_external_presence_data(data)

        #self.canvas.pack(0,0)
        #self.canvas.pack(side="left", fill="both", expand=True)
        self.canvas.place(x=150,y=120)

        self.myEntryBox.focus_set()
        self.myEntryBox.delete(0, 'end')

    def read_config_file(self):
        with open('edempresence.yaml', 'r') as config:
            self.configs = yaml.load(config)


root = tk.Tk()
root.geometry("600x680")

mf = EdemPresenceGUI(root)

root.mainloop()
