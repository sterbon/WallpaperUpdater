import os
import ctypes
import urllib.request, json 

#Name of subbreddit
subreddit = 'wallpapers'

with urllib.request.urlopen("https://www.reddit.com/r/"+ str(subreddit) + "/top.json") as url:
    data = json.loads(url.read().decode())
    url = data["data"]["children"][0]["data"]["url"]

urllib.request.urlretrieve(url, 'wallpaper.jpg')

#Set wallpaper
ctypes.windll.user32.SystemParametersInfoW(20, 0, 'E:\wallpaper.jpg' , 0)
