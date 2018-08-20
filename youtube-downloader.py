import os
import subprocess #command 실행해야되므로
import pytube


videoUrl = input("다운받을 url을 입력하세요")
yt = pytube.YouTube(videoUrl) #다운받을 url
videos = yt.streams.all()

for i in range(len(videos)) : 
    print(i, ' , ', videos[i])

down_dir = "/Users/wonboklee/Desktop/Python/examples_inflearn"

cNum = int(input("다운받을 화질은?(0~21입력)"))

videos[cNum].download(down_dir)

newFilename = input("변환 할 mp3파일 명 입력")
originalFilename = videos[cNum].default_filename

subprocess.call([
    'ffmpeg', '-i', os.path.join(down_dir, originalFilename),
    os.path.join(down_dir, newFilename)
])

print("동영상 다운 및 mp3변환 완료")
