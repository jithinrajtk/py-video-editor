from moviepy.editor import VideoFileClip, concatenate_videoclips, sys
 
clip1 = VideoFileClip(sys.argv[1])

clip2 = VideoFileClip(sys.argv[2])
 
final_clip = concatenate_videoclips([clip1,clip2]) 

final_clip.write_videofile("finalout.mp4")      


####################################################

#from moviepy.editor import *
#import sys

#logMessage='Files order List:'+str(sys.argv)
#print('\x1b[6;30;42m' + logMessage+ '\x1b[0m')

#print 

#Intro video location
#intro=VideoFileClip(sys.argv[1])

#Content video location
#content=VideoFileClip(sys.argv[2])

#finalrender = concatenate_videoclips([intro,content])
#finalrender.write_videofile('finalclass.mp4', codec='libx264')