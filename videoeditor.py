from moviepy.editor import *

#Content video location
content_name = input("Enter content video name: ") 
content = VideoFileClip(content_name)

#Intro video location
intro_name = input("Enter intro video name: ") 
intro = VideoFileClip(intro_name)

#Video concatenation function
finalrender = concatenate_videoclips([intro,content])
finalrender.write_videofile('finalclass.mp4', codec='libx264')