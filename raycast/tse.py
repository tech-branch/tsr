#!/usr/bin/env /usr/bin/python3

# Required parameters:
# @raycast.schemaVersion 1
# @raycast.title tse
# @raycast.mode compact

# Optional parameters:
# @raycast.icon 📝
# @raycast.packageName Timestamp Recorder Editor

# Documentation:
# @raycast.description Edit your TSR entries
# @raycast.author Tomasz Sobota
# @raycast.authorURL https://techbranch.net

import os
import webbrowser

home_path = os.path.expanduser('~')
REPOSITORY_PATH = home_path + "/tsr"

webbrowser.open('file://' + os.path.realpath(REPOSITORY_PATH))
print("Opening")
