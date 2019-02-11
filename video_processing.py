import time
import os

#3. Add screen_between.jpg at 1 minute boundary of sample.mp4
import cv2
import subprocess

video_file_name = "endout.mp4" 
between_screen = "screen_between.jpg"
vid = cv2.VideoCapture(video_file_name)
height = vid.get(cv2.CAP_PROP_FRAME_HEIGHT)
width = vid.get(cv2.CAP_PROP_FRAME_WIDTH)

subprocess.call(("""ffmpeg -y -i %s \
-i %s \
-filter_complex "[1]scale=%s:%s[b];[0][b] overlay=0:0:enable='lt(mod((t\),20),1)'" \
between_output.mp4""")%(video_file_name, between_screen, width,height), shell=True)

time.sleep(1)

#1. Add screen_start.jpg at start of sample.mp4
import cv2
import subprocess

video_file_name = "between_output.mp4" 
start_screen = "screen_start.jpg"
vid = cv2.VideoCapture(video_file_name)
height = vid.get(cv2.CAP_PROP_FRAME_HEIGHT)
width = vid.get(cv2.CAP_PROP_FRAME_WIDTH)

subprocess.call(('ffmpeg -y -loop 1 -framerate 24 -t 5 -i %s \
-i %s \
-filter_complex "[0]scale=%s:%s,setsar=1[im];[1]scale=%s:%s,setsar=1[vid];[im][vid]concat=n=2:v=1:a=0" \
startout.mp4')%(start_screen, video_file_name, width, height, width, height),shell=True)

time.sleep(1)
os.remove("between_output.mp4")


# 2. Add screen_end.jpg at end of sample.mp4
import cv2
import subprocess
video_file_name = "startout.mp4" 
end_screen = "screen_end.jpg"  
vid = cv2.VideoCapture(video_file_name)
height = vid.get(cv2.CAP_PROP_FRAME_HEIGHT)
width = vid.get(cv2.CAP_PROP_FRAME_WIDTH)


subprocess.call(('ffmpeg -y -i %s \
-loop 1 -framerate 24 -t 5 -i %s \
-filter_complex "[0]scale=%s:%s,setsar=1[im];[1]scale=%s:%s,setsar=1[vid];[im][vid]concat=n=2:v=1:a=0" \
endout.mp4')%(video_file_name, end_screen, width, height, width, height),shell=True)

time.sleep(1)
os.remove("startout.mp4")

#4. Add this text "This is a watermark text" at the center of video
import subprocess
video_file_name = "endout.mp4" 
text_format = "comic.ttf"
text = "This video is original"
subprocess.call(("""ffmpeg -y -i %s -vf drawtext="fontfile=%s: \
text=%s: fontcolor=white: fontsize=24: box=1: boxcolor=black@0.5: \
boxborderw=5: x=(w-text_w)/2: y=(h-text_h)/2" -codec:a copy watermarkoutput.mp4""")%(video_file_name, text_format, text), shell =True)

time.sleep(1)
os.remove("endout.mp4")

#5. Add logo.jpg at the left top corner of video
import subprocess
video_file_name = "watermarkoutput.mp4" 
logo_file_name = "logo.jpg"
subprocess.call(('ffmpeg -y -i %s -i %s -filter_complex \
"overlay=5:5" \
-codec:a copy sample_updated.mp4')%(video_file_name, logo_file_name), shell =True)

os.remove("watermarkoutput")



