# Video-Player-Grid
This is a website that has a main video player at the top and a grid of selectable videos underneath.

## Requirements

* Python 3
* ffmpeg

## To Use
Ensure that the *index.html* and *callClip.js* files and the thumbnails folder have write permissions.

The other files in "docs" folder and the video files in "clip_mp4" folder require at least read permissions.

Provide clips ending in ".mp4". Ffmpeg will automatically generate thumbnails from videos, or alternatively, provide thumbnails whose names match the clips' names and end in ".png".

* Drop clips in the "clips_mp4" folder.
* Run the *createClipsPaths* Python script.

## About the Project Structure

This is meant to be a simple deployment of a website which can read, show and allow playback of a collection of videos. No back-end API required, much of the setup is automated via Python, with the webpage running only on minimal HTML, CSS and Javascript.
