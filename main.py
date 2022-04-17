import time
import tkinter
import cv2   # pip install opencv-python
import PIL.Image, PIL.ImageTk   # pip install pillow
from functools import partial
import threading
import imutils
stream = cv2.VideoCapture("video/pubg.mp4")
flag = True
def play(speed):
    global flag
    print(f"chake speed is {speed}")

        # play the video in reverse mode
    frame1 = stream.get(cv2.CAP_PROP_POS_FRAMES)
    stream.set(cv2.CAP_PROP_POS_FRAMES,frame1 + speed)
    grabbed, frame = stream.read()
    if not grabbed:
        exit()
    frame = imutils.resize(frame, width=SET_WIDTH, height=SET_HEIGHT)
    frame = PIL.ImageTk.PhotoImage(image=PIL.Image.fromarray(frame))
    canvas.image = frame
    canvas.create_image(0, 0, image=frame, anchor=tkinter.NW)
    if flag:
        canvas.create_text(134,25, fill="black", font="Times 26 bold", text="Decision Pending")
    flag = not flag
        # play the video in forward mode
def pending(decision):
    # 1. Display decision pending image
    frame = cv2.cvtColor(cv2.imread("img/pendind.png"), cv2.COLOR_BGR2RGB)
    frame = imutils.resize(frame, width=SET_WIDTH, height=SET_HEIGHT)
    frame = PIL.ImageTk.PhotoImage(image=PIL.Image.fromarray(frame))
    canvas.image = frame
    canvas.create_image(0, 0, image=frame, anchor=tkinter.NW)
    time.sleep(1)


    # 2. Wait for 1 second
    # 3. Display sponsor img
    frame = cv2.cvtColor(cv2.imread("img/sponsor.png"), cv2.COLOR_BGR2RGB)
    frame = imutils.resize(frame, width=SET_WIDTH, height=SET_HEIGHT)
    frame = PIL.ImageTk.PhotoImage(image=PIL.Image.fromarray(frame))
    canvas.image = frame
    canvas.create_image(0, 0, image=frame, anchor=tkinter.NW)
    time.sleep(1)

    # 4. wait for 1.5 second
    # 3. Display out/notout img
    if decision == 'out':
        decisionImg = "img/out.png"
    else:
        decisionImg = "img/not_out.png"
    frame = cv2.cvtColor(cv2.imread(decisionImg), cv2.COLOR_BGR2RGB)
    frame = imutils.resize(frame, width=SET_WIDTH, height=SET_HEIGHT)
    frame = PIL.ImageTk.PhotoImage(image=PIL.Image.fromarray(frame))
    canvas.image = frame
    canvas.create_image(0, 0, image=frame, anchor=tkinter.NW)
    time.sleep(1)

    # 4. wait for 1.5 second

    pass
def out():
    thread = threading.Thread(target=pending, args=("out",))
    thread.daemon = 1
    thread.start()
    print("Player is out")
def not_out():
    thread = threading.Thread(target=pending, args=("not out",))
    thread.daemon = 1
    thread.start()
    print("Player is not out")
# Width and height of our main screen
SET_WIDTH = 650
SET_HEIGHT = 368

# TKinter gui starts here
window = tkinter.Tk()
window.title("CodeWithSwaraj Third Umpire Decision Review Kit")
cv_img = cv2.cvtColor(cv2.imread("img/welcome.png"),cv2.COLOR_BGR2RGB)
canvas = tkinter.Canvas(window, width=SET_WIDTH, height=SET_HEIGHT)
photo = PIL.ImageTk.PhotoImage(image=PIL.Image.fromarray(cv_img))
image_on_canvas = canvas.create_image(0, 0, ancho=tkinter.NW, image=photo)
canvas.pack()

# Buttons to control playback
btn = tkinter.Button(window,text="<< Previous (fast)",width=50, command=partial(play, -25))
btn.pack()
btn = tkinter.Button(window,text="<< Previous (slow)",width=50, command=partial(play, -2))
btn.pack()
btn = tkinter.Button(window,text="Next (slow) >>",width=50, command=partial(play, 2))
btn.pack()
btn = tkinter.Button(window,text="Next (fast) >>",width=50, command=partial(play, 25))
btn.pack()
btn = tkinter.Button(window,text="Give Out",width=50, command=out)
btn.pack()
btn = tkinter.Button(window,text="Give Not Out",width=50, command=not_out)
btn.pack()
window.mainloop()