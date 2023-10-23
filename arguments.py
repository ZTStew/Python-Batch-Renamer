"""
Description:
  Object handles command line arguments, stores them together for reference
"""

import glob, os, argparse

class Arguments:
  def __init__(self):
    # Handles command line options/arguments
    args = argparse.ArgumentParser(description="Program searches given folder for video files and trims a specified number of seconds from the start or the end of the video. The file is then saved in a specified location.")

    # command line option for phrase_to_remove
    args.add_argument(
      "-p",
      "--phrase",
      type=str,
      help="Phrase To Remove: str -> The exact string to search for to replace"
    )

    # command line option for replace_with
    args.add_argument(
      "-r",
      "--replace",
      type=str,
      help="Replace With: str -> What the identified phrase will be replaced with. If want to replace the phrase with nothing, type \"blank\", if want to replace the phrase with a space, type \"space\""
    )

    # command line option for replace_with
    args.add_argument(
      "-f",
      "--file_type",
      type=str,
      help="File Type: str -> The file type that will be searched for the specified phrase"
    )

    self.args = args.parse_args()

    self.phrase_to_remove = "test"
    # What will replace the searched phrase
    self.replace_with = ""
    # Extension of files being searched
    self.file_type = "mp4"
    # Directory to search for files
    self.directory = "./"

    self.assign_args()

    # Collects all files in given directory with matching extension
    self.input_files = glob.glob(f"{self.directory}/*." + self.file_type)


  # Method overwrites default variables with values proveded by users
  def assign_args(self):
    # assigns phrase_to_remove value
    if self.args.phrase:
      self.phrase_to_remove = self.args.phrase

    # assigns replace_with value
    if self.args.replace:
      if self.args.replace.lower() == "blank":
        self.replace_with = ""
      elif self.args.replace.lower() == "space":
        self.replace_with = " "
      else:
        self.replace_with = self.args.replace

    # assigns file_type value
    if self.args.file_type:
      self.file_type = self.args.file_type.strip(".")