# Content Warning webm to mp4 converter

This project will automatically convert all the webm files that get saved to your desktop from content warning to mp4 files. This makes sharing easier in platforms like Messenger, where there is no sound when you upload webm files.

### Prerequisites

If you only want the executable to work, you can install [ffmpeg](https://phoenixnap.com/kb/ffmpeg-windows).
For the Python code to work, you need to have the following software installed 
* [Python](https://www.python.org/downloads/)
* [pip](https://pip.pypa.io/en/stable/installation/)
* [ffmpeg](https://www.ffmpeg.org/download.html)

If you're stuck on installing ffmpeg, You can check out this guide on [Installing ffmpeg on windows](https://phoenixnap.com/kb/ffmpeg-windows)

After that, install ffmpeg-python using this command in your command line
```
pip install ffmpeg-python
```

### Running

If you're using the executable, you just have to click it. Refer to the rest of the instructions for getting the python code to work

The desktop variable is the directory that contains the videos, change it if the content warning videos aren't stored here
```
desktop = os.path.expanduser("~/Desktop/")
```

Change the output directory to wherever you want to store the mp4 videos on
```
output_directory = 'D:/content_vids/'
```

After that, you can run the code by typing this in your command line:
```
py webm_mp4converter.py
```

