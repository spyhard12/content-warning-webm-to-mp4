import ffmpeg
import os
import os.path
import fnmatch
import subprocess

# if this doesn't work, just change it to a string containing the directory of the videos
# desktop = 'D:/Users/{username}/Desktop'
desktop = os.path.expanduser("~/Desktop/")

# change output directory where you want the videos to go
output_directory = 'D:/content_vids/'

def convert_all_desktop(directory, filetype):
  for file in os.listdir(directory):
    if fnmatch.fnmatch(file, filetype):
      output_file = output_directory + file.replace('.webm', '.mp4')

      isFile = os.path.isfile(output_file)

      if not isFile:
        print(output_file)
        (
          ffmpeg
            .input(directory + file)
            .output(output_file)
            .run()
        )

      os.remove(directory + file)

try:
  os.makedirs(output_directory)
  print("folder made")
except:
  print("folder already made")
  pass

convert_all_desktop(desktop, '*.webm')
