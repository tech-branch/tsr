#!/usr/bin/env /usr/local/bin/python3.9

# Required parameters:
# @raycast.schemaVersion 1
# @raycast.title tsn
# @raycast.mode compact

# Optional parameters:
# @raycast.icon 📝
# @raycast.argument1 { "type": "text", "name":"notes", "placeholder": "note content" }
# @raycast.packageName Timestamp Recorder Notes

# Documentation:
# @raycast.description Simple file-based notes for the ts recorder
# @raycast.author Tomasz Sobota
# @raycast.authorURL https://techbranch.net

import datetime
import sys
import os

# ------------
#  PARAMETERS
# ------------
# modify to your preference

FILE_PATH = "../records/notes.csv"


# ----------------------------
#  Read the script parameters
#

notes = ""

try:
  # read notes from input
  notes = sys.argv[1]
except IndexError:
  # no notes provided
  notes = "no note provided"

if notes == "":
  # if we're still seeing empty notes list
  notes = "no note provided"

# ---------

timestamp = str(datetime.datetime.now())

output = f"\n{timestamp},{notes}"

# make sure directories exist
os.makedirs(os.path.dirname(FILE_PATH), exist_ok=True)

# plain text output
text_file = open(FILE_PATH, "a")
_ = text_file.write(output)
text_file.close()
