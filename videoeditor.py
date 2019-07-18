from moviepy.editor import *

#Content video location
second_video = input("Enter first video name: ") 
video_two = VideoFileClip(second_video)

#Intro video location
first_video = input("Enter intro video name: ") 
video_one = VideoFileClip(first_video)

#Video concatenation function
finalrender = concatenate_videoclips([video_two,video_one])
finalrender.write_videofile('finalvideo.mp4', codec='libx264')

print ('Video joined successfully!!')