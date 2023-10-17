import os, glob, sys

"""
Arguments:
  Phrase: String
  Replace With: String
  File Type: String
"""

help_flag = False

if len(sys.argv) > 1:
  # Prints how to use program into command line
  if sys.argv[1].lower() == "help":
    print("Arguments:\n  Phrase: String\n  Replace With: String\n  File Type: String")
    print("If want to replace the phrase with nothing, type \"blank\", if want to replace the phrase with a space, type \"space\"")

    help_flag = True

if not help_flag:
  # default argument values
  phrase_to_remove = "www"
  replace_with = ""
  file_type = "mp4"

  # phrase
  if len(sys.argv) > 1:
    phrase_to_remove = sys.argv[1].strip()
  # replace with
  if len(sys.argv) > 2:
    if sys.argv[2].lower() == "blank":
      replace_with = ""
    elif sys.argv[2].lower() == "space":
      replace_with = " "
    else:
      replace_with = sys.argv[2].strip()
  # file type
  if len(sys.argv) > 3:
    file_type = sys.argv[3].strip(".")

  print("phrase: " + phrase_to_remove)
  print("replace: " + replace_with)
  print("file: " + file_type)


  # gets all files in directory
  directory = "./"
  input_files = glob.glob(f"{directory}/*." + file_type)
  # print(input_files)

  # function removes "phrase_to_remove" from "phrase" and replaces it with "replace_with" and re-adds "file_type"
  def remove_phrase(phrase, phrase_to_remove, replace_with, file_type):
    # cuts phrase based on phrase_to_remove
    cut = phrase.split(phrase_to_remove)
    out = ""

    # loops through cut and reconstructs new phrase
    val = 0
    while val < len(cut):
      # adds each index to out
      out += cut[val]

      val += 1
      # prevents replace_with from being added to the end of the phrase
      if val < len(cut):
        out += replace_with

    out = out.strip()

    out += "." + file_type

    return out

  # Itterates through all file_type files found in given directory
  for input_file in input_files:
    # removes file extension from input_file name
    renamed_file = input_file.split("." + file_type)[0]
    # removes any trailing whitespaces
    renamed_file = renamed_file.strip()
    # removes file path from renamed_file
    renamed_file = os.path.basename(renamed_file)

    # checks if phrase_to_remove is found in file name 
    if phrase_to_remove in renamed_file:
      # removes phrase
      update_file = remove_phrase(renamed_file, phrase_to_remove, replace_with, file_type)
      # updates existing file with new name
      os.rename(input_file, update_file)
      print("Task completed: " + input_file + " -> " + update_file)
    # else:
    #   print("skip")
