import glob 
import os

stringa = ""
for f in glob.glob("*.mp4"):
    stringa += f + "|"

os.system("ffmpeg -i \"concat:" + stringa + "\" -codec copy output.mp4")