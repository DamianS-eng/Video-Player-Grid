### 18 May, 2023
### for Video Clips
import re
import os
import os.path
import random

dir_path = os.path.dirname(os.path.abspath(__file__))
clips = "clip_mp4"
thumbnails = "thumbnails"
pre_folder = "docs\\"
full_clips= os.path.join(dir_path, clips)
full_thumbnails=  os.path.join(dir_path, thumbnails)
index_start= os.path.join(dir_path, pre_folder +".index_start")
index_file = "index.html"
index_end= os.path.join(dir_path, pre_folder +".index_end")
js_file = os.path.join(dir_path, pre_folder + "callClip.js")

error_txt= os.path.join(dir_path,".thumbError.txt")
scale = 160

def shuffledList(sample):
    theNewlist = []
    for clip in os.listdir(full_clips):
        if clip.endswith(".mp4"):
            theNewlist.append(clip)
    random.shuffle(theNewlist)  
    if (sample > 1):
        someofthelist = random.sample(theNewlist, sample) 
        return (someofthelist)
    return (theNewlist)

def createThumbnails():
    totalClips = len(os.listdir(full_clips))
    for clip in os.listdir(full_clips):
        if clip.endswith(".mp4"):
            stringToOS="ffmpeg -y -i "+ full_clips + "/" + clip +" -ss 00:00:01.000 -vframes 1 -vf scale="+ str(scale) +":-1 "+ thumbnails +"/"+ clip[0:-4] +".png > out.txt 2>>" + error_txt
            os.system(stringToOS)
    totalThumbs = len(os.listdir(full_thumbnails))
    if(totalClips > totalThumbs):
        print("Umm...\nOut of "+ str(totalClips) + ", " + str(totalThumbs) + " thumbnails were created.\nCheck the thumbError txt.")
    return

#write each line of div containing thumbnail path and source name for JS to change main player's video

def insertClipThumbnails():
    clipList= ""
    tabs="\t\t\t\t"
    template_div= tabs + """<div class="flow"> 
""" + tabs + """\t<button href="#" onclick="showImage('"""
    for clip in shuffledList(0):
        if clip.endswith(".mp4"):
            clipList = clipList + template_div + clip[0:-4] + "')\" tabindex=0> <img src=\"../" + thumbnails + "/" + clip[0:-4] + ".png\" alt=\"" + clip[0:-4] + "\" id=\"" + clip[0:-4]
            clipList = clipList + """\"></button>\n"""+tabs+"""</div>\n"""
    return(clipList)

#Generate a JS readable array of the local file paths pointing to each elegible video and thumbnail, which share the same name but have a different file extension.
#    let sidebar = document.getElementById("stage-sidebar");
#    let chosen_name = document.getElementById(imgName);
#    chosen_name.textContent = imgthumb;
#   chosen_name.textContent = inim;

def writeJS_arrayofclips():
#find each -.mp4 file in the directory and append to js list
    clipList=""
    print(str(len(os.listdir(full_clips))) + " clips found.")
    if len(os.listdir(full_clips)) <= 0:
        return("")
    for clip in os.listdir(full_clips):
        if clip.endswith(".mp4"):
            clipList = clipList + clip[0:-4] + "', '"
    clipList = clipList[0:-3] + "]; \n"
    return(clipList);

def writeJSfunc():
    arrayOfClips = "const clipsList = ['" + writeJS_arrayofclips();
    script = arrayOfClips + """
const video_source = \"""" + clips + """/";
const thumb_source = \"""" + thumbnails + """/";
"""
    return(script)

def writeHTML_1():
    goingToHTML = ""
    writingOrder = [open(index_start, "r").read(), 
        insertClipThumbnails(), 
        open(index_end, "r").read()]
    for i in writingOrder:
        goingToHTML = goingToHTML + i
    return(goingToHTML)

#this will write list of img links to HTML
#uncomment to allow a quick run through Python
if __name__ == "__main__":
    open(js_file, "w").write(writeJSfunc())
    open(index_file, "w").write(writeHTML_1())
    createThumbnails();
