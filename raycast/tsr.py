#!/usr/bin/env /usr/local/bin/python3.9

# Required parameters:
# @raycast.schemaVersion 1
# @raycast.title tsr
# @raycast.mode compact

# Optional parameters:
# @raycast.icon ⏰
# @raycast.argument1 { "type": "text", "name":"tags", "placeholder": "optional tags", "optional": true }
# @raycast.packageName Timestamp Recorder

# Documentation:
# @raycast.description Simple file-based ts recorder with tags
# @raycast.author Tomasz Sobota
# @raycast.authorURL https://techbranch.net

import datetime
import sys
import os

# ------------
#  PARAMETERS
# ------------
# modify to your preference

FILE_PATH = "../records/record.csv"


# ----------------------------
#  Read the script parameters
#

tags = ""

try:
  # read tags from input
  tags = sys.argv[1]
except IndexError:
  # no tags provided
  tags = "next"

if tags == "":
  # if we're still seeing empty tags list
  tags = "next"

# ---------

timestamp = str(datetime.datetime.now())

output = f"\n{timestamp},{tags}"

# make sure directories exist
os.makedirs(os.path.dirname(FILE_PATH), exist_ok=True)

# plain text output
text_file = open(FILE_PATH, "a")
_ = text_file.write(output)
text_file.close()
