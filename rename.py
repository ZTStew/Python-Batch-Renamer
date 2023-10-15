import os, glob

"""
Arguments:
  Phrase: String
  File Type: String

"""

directory = "./"
input_files = glob.glob(f"{directory}/*.mp4")

# Temp Variables:
remove_phrase = "www"
file_type = "mp4"

# Itterates through all .mp4 files found in given directory
for input_file in input_files:
  file_name = os.path.basename(input_file)
  print(file_name)
