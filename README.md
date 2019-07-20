# py-video-editor
Python Script to join / concatenate video files

## Dependencies 
* moviepy - https://zulko.github.io/moviepy/
* ffmpeg - https://gpac.wp.mines-telecom.fr/mp4box/

## Installation
### On Linux

For Python3
`$ pip3 install moviepy`

For Python2
`$ pip install moviepy`

For ffmpeg
`$ sudo apt-get install ffmpeg`

### On Mac

For Python3
`$ pip3 install moviepy`

For Python2
`$ pip install moviepy`

For ffmpeg
`$ brew install ffmpeg` 

## Usage
### Using moviepy
* Add file names as command line arguments like example below.Dont forget to include the extension</br>
* Run `$ python videoeditor.py intro.mp4 content.mp4 outer.mp4`

### Using ffmpeg
* Add file names to a text file. Refer list.txt file
* Run `$ ffmpeg -f concat -safe 0 -protocol_whitelist file,http,https,tcp,tls,crypto -i list.txt -c copy outfile.mp4 -n`

### Acknowledgements 
This is made using moviepy library
