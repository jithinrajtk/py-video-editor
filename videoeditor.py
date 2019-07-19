from moviepy.editor import *
import sys

logMessage='Files order List:'+str(sys.argv)
print('\x1b[6;30;42m' + logMessage+ '\x1b[0m')

print 

#Intro video location
intro=VideoFileClip(sys.argv[1])

#Content video location
content=VideoFileClip(sys.argv[2])

#Outer video location
outer=VideoFileClip(sys.argv[3])

finalrender = concatenate_videoclips([intro,content,outer])
finalrender.write_videofile('finalclass.mp4', codec='libx264')
print('\x1b[6;30;42m' + 'Success' + '\x1b[0m')
