from tkinter import *
import os
import ctypes
import urllib.request
import json
from PIL import Image, ImageTk
from io import BytesIO
from urllib.request import urlopen
import pkg_resources.py2_warn

class MyWindow:
    def __init__(self, win):
        self.lbl1 = Label(win, text='r/', bg='gray')
        self.t1 = Entry(bd=3)
        self.lbl1.place(x=400, y=50)
        self.t1.place(x=420, y=50)
        self.b1 = Button(win, text='Fetch', command=self.getImg)
        self.b1.place(x=550, y=48)

    def getImg(self):
        d=[]
        url = "https://www.reddit.com/r/" + self.t1.get() + "/top/.json"
        print(url)
        req = urllib.request.Request(url,
                                     data=None,
                                     headers={'User-Agent': 'sterbon'})
        f = urllib.request.urlopen(req)
        data = json.loads(f.read().decode())

        # Load all images
        for i in range(4):
            d.append(data["data"]["children"][i]["data"]["url"])
            print(d)
            u = urlopen(d[i])
            raw_data = u.read()
            print(i)
            im = Image.open(BytesIO(raw_data))
            photo = ImageTk.PhotoImage(im.resize((200, 150)))
            label = Label(image=photo)
            label.image = photo
            button = Button(window, image=photo,
                            command=lambda i=i: self.setwall(d[i]))
            button.place(x=60+i*220, y=150)
            label.place(x=60+i*220, y=150)
            u.close()

    def setwall(self, imgUri):
        print("clicked", imgUri)
        urllib.request.urlretrieve(imgUri, 'wallpaper.jpg')
        # Set wallpaper
        currentWall = os.getcwd()+"\wallpaper.jpg"
        ctypes.windll.user32.SystemParametersInfoW(20, 0, currentWall, 0)


window = Tk()
mywin = MyWindow(window)
window.configure(background='gray')
window.title('Wallpaper Setter')
window.geometry("1000x400")
window.mainloop()
