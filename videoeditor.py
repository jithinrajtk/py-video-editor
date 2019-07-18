from moviepy.editor import *

#Content video location
content_loc = input("Enter content video location: ") 
content=VideoFileClip(content_loc)

#Intro video location
intro_loc =input("Enter Intro video location: ") 
intro=VideoFileClip(intro_loc)

finalrender = concatenate_videoclips([intro,content,intro])
finalrender.write_videofile('finalclass.mp4', codec='libx264')