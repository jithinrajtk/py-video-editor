from moviepy.editor import *
content = VideoFileClip('class.mp4')
intro = VideoFileClip('intro.mp4')
finalrender = concatenate_videoclips([intro,content,intro])
finalrender.write_videofile('finalclass.mp4', codec='libx264')