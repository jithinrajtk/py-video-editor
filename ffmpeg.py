import os
myCmd = 'ffmpeg -f concat -safe 0 -protocol_whitelist file,http,https,tcp,tls,crypto -i list.txt -c copy outfile.mp4 -n'
os.system(myCmd)