from tkinter import *
from tkinter import ttk
from PIL import ImageTk, Image

# Create a new Tkinter window
window = Tk()

# Set the window size and title
window.geometry("1440x900")
window.title("OTUS UAV")


# Create an image object from a file
bg_image = PhotoImage(file="bg_img.png")
# Create a label for the background image
background_image = Label(window, image=bg_image)
background_image.place(x=0, y=0, relwidth=1, relheight=1)

# Create a frame for the first picture
frame1 = Frame(window, width=500, height=279)
frame1.config(bd=2)
frame1.place(x=50, y=50)

# Create an image object from a file
uav_img = PhotoImage(file="uav.png")
# Create a label for the first picture
label1 = Label(frame1, image=uav_img)
# Fit the image to the frame size
label1.place(x=0, y=0, relwidth=1, relheight=1)

# Create four buttons for the first picture
frame_but1 = Frame(window)
frame_but1.place(x=50,y=350)
button1 = Button(frame_but1, text="Manuel Kilitlenme")
button1.config(width=15, height=3)
button1.pack(side=LEFT)

frame_but2 = Frame(window)
frame_but2.place(x=170,y=350)
button2 = Button(frame_but2, text="Takip Et")
button2.config(width=15, height=3)
button2.pack(side=LEFT)

frame_but3 = Frame(window)
frame_but3.place(x=290,y=350)
button3 = Button(frame_but3, text="DISARM ET")
button3.config(width=15, height=3, bg="red")
button3.pack(side=LEFT)

frame_but4 = Frame(window)
frame_but4.place(x=410,y=350)
button4 = Button(frame_but4, text="Seç")
button4.config(width=15, height=3)
button4.pack(side=LEFT)

frame_but_start = Frame(window)
frame_but_start.place(x=50,y=420)
button_start = Button(frame_but_start, text="Göreve Başla")
button_start.config(width=15, height=3)
button_start.pack()

# Create a frame for the second picture
frame2 = Frame(window, width=250, height=360)
frame2.config(bd=2)
frame2.place(x=650, y=50)

# Create an image object from a file
img2 = PhotoImage(file="ortapanel.png")
# Create a label for the second picture
label2 = Label(frame2, image=img2)
label2.place(x=0, y=0, relwidth=1, relheight=1)

# Create a slider with values in the range of 0 to 1000
frame_slid = Frame(window)
frame_slid.place(x=700, y=470)
slider = Scale(frame_slid, from_=0, to=1000, orient=HORIZONTAL)
slider.pack()

# Create a button for the second picture
frame_but5 = Frame(window)
frame_but5.place(x=700,y=420)
button5 = Button(frame_but5, text="Gönder")
button5.config(width=20, height=2)
button5.pack()

# Create a frame for the third picture
frame3 = Frame(window, width=430, height=700)
frame3.config(bd=2)
frame3.place(x=970, y=50)

# Create an image object from a file
map_img = PhotoImage(file="map.png")
# Create a label for the third picture
label3 = Label(frame3, image=map_img)
label3.place(x=0, y=0, relwidth=1, relheight=1)

# Start the GUI event loop
window.mainloop()
