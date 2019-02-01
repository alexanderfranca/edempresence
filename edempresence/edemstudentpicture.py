from tkinter import Tk, Canvas
from PIL import ImageTk, Image

class EdemStudentPicture:

    def __init__(self, filepath=None):

        self.filepath = filepath 

        root = Tk()

        #Create a canvas
        canvas = Canvas(root, width=400, height=300)
        canvas.pack()

        # Load the image file
        im = Image.open(filepath)
        # Put the image into a canvas compatible class, and stick in an
        # arbitrary variable to the garbage collector doesn't destroy it
        canvas.image = ImageTk.PhotoImage(im)
        # Add the image to the canvas, and set the anchor to the top left / north west corner
        canvas.create_image(0, 0, image=canvas.image, anchor='nw')

        root.mainloop()



