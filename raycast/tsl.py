#!/usr/bin/env /usr/local/bin/python3.9

# Required parameters:
# @raycast.schemaVersion 1
# @raycast.title tsl
# @raycast.mode compact

# Optional parameters:
# @raycast.icon ⏰
# @raycast.packageName Timestamp Recorder Current

# Documentation:
# @raycast.description Check what's your latest activity and how much time passed
# @raycast.author Tomasz Sobota
# @raycast.authorURL https://techbranch.net

import datetime
import csv
import os

# ------------
#  PARAMETERS
# ------------
# modify to your preference

FILE_PATH = "../records/record.csv"

# ---------

current_timestamp = datetime.datetime.now()

output = f""

# make sure directories exist
os.makedirs(os.path.dirname(FILE_PATH), exist_ok=True)

with open(FILE_PATH, "r") as csvfile:
    reader = csv.reader(csvfile)
    for row in reader:
        # print(', '.join(row))
        raw_datetime = row[0]
        raw_tags = row[1]

        parsed_datetime = datetime.datetime.fromisoformat(raw_datetime)
        dt_delta = current_timestamp - parsed_datetime
        dt_total_minutes = int(round(dt_delta.total_seconds()/60, 0))
        dt_hours = int(dt_total_minutes/60)
        dt_minutes = dt_total_minutes-dt_hours*60

        delta_pretty = f"{dt_hours}h {dt_minutes}m"
        # that way we'll only see the last entry:
        output = f"{raw_tags} since {delta_pretty} ago"

print(output)
