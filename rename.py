import os, sys
from arguments import Arguments

"""
Arguments:
  Phrase: String
  Replace With: String
  File Type: String
"""

arg = Arguments()
errors = []

print("Search Phrase: " + arg.phrase_to_remove)
print("Prase Replace: " + arg.replace_with)
print("File Type: " + arg.file_type)


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
for input_file in arg.input_files:
  # Gitbash is unable to handle non-unicode symbols potentially crashing the program
  try:
    # removes file extension from input_file name
    renamed_file = input_file.split("." + arg.file_type)[0]
    # removes any trailing whitespaces
    renamed_file = renamed_file.strip()
    # removes file path from renamed_file
    renamed_file = os.path.basename(renamed_file)

    # checks if phrase_to_remove is found in file name 
    if arg.phrase_to_remove in renamed_file:
      # removes phrase
      update_file = remove_phrase(renamed_file, arg.phrase_to_remove, arg.replace_with, arg.file_type)
      # updates existing file with new name
      os.rename(input_file, update_file)
      print("Task completed: " + input_file + " -> " + update_file)

  except:
    errors.append(input_file)

# Informs user there are errors that occured
if len(errors) > 0:
  print("ERRORS Detected: " + str(len(errors)))
