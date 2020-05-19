import os
import ctypes
import urllib.request, json 
import PySimpleGUI as sg

form = sg.FlexForm('Wallpaper Downloader')

layout = [ [sg.Text('r/'), sg.InputText()],
           [sg.OK()],
           [sg.Cancel()] ]

button, name = form.Layout(layout).Read()
print(name[0])
#Name of subbreddit
subreddit = 'wallpapers'
url = "https://www.reddit.com/r/"+ str(name[0]) + "/top.json"
print(url)
with urllib.request.urlopen(url) as url:
    data = json.loads(url.read().decode())
    url = data["data"]["children"][0]["data"]["url"]

urllib.request.urlretrieve(url, 'wallpaper.jpg')

#Set wallpaper
ctypes.windll.user32.SystemParametersInfoW(20, 0, 'E:\Projects\WallpaperSetter\wallpaper.jpg' , 0)
