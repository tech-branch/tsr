#!/usr/bin/env /usr/bin/python3

# Required parameters:
# @raycast.schemaVersion 1
# @raycast.title tsv
# @raycast.mode compact

# Optional parameters:
# @raycast.icon ⏰
# @raycast.packageName Timestamp Recorder HTML view

# Documentation:
# @raycast.description Compile your records into an HTML table
# @raycast.author Tomasz Sobota
# @raycast.authorURL https://techbranch.net

import datetime
import webbrowser
import csv
import os


# ------------
#  PARAMETERS
# ------------
# modify to your preference

TSR_FILE_PATH = "../records/record.csv"
TSN_FILE_PATH = "../records/notes.csv"
HTML_OUTPUT_PATH = "../records/record.html"


# ---------
#  Helpers
# ---------

# Enum representing either TSR or TSN
class RecordType:
    TSR = 1
    TSN = 2

# function assigning side to a record type
def get_side(record_type: int, default = "left"):
    if record_type == RecordType.TSR:
        return "left"
    elif record_type == RecordType.TSN:
        return "right"
    else:
        return default

def csv_to_timeline_entries(trows: list, side: str = "left"):
    containers = []
    for row in trows:
        
        ts_side = get_side(row[2], side)
        pretty_date = row[0].strftime('%H:%M on %d %b %Y')

        html_container = f'<div class="container {ts_side}">\n<div class="content">\n'
        html_container += f'<h2>{row[1]}</h2>\n'
        html_container += f'<p>{pretty_date}</p>\n'
        html_container += '</div>\n</div>\n'
        
        containers.append(html_container)
    # return containers as a single string with reversed order
    return "".join(containers[::-1])


def generate_html_template(html_table: str):
    html_template = f"""<!DOCTYPE html>
    <html>
    <head>
    <link rel="stylesheet" href="../assets/timeline.css">
    </head>
    <body>

    <div class="timeline">
        {html_table}
    </div> 

    </body>
    </html>"""
    return html_template

def html_template_to_file(html_template: str, file_path: str):
    """Save html template to file"""
    fp = ""
    if file_path == None:
        fp = HTML_OUTPUT_PATH
    else:
        fp = file_path
    
    with open(fp, "w") as f:
        f.write(html_template)


# ------
#  Main
# ------

# make sure directories exist
os.makedirs(os.path.dirname(TSR_FILE_PATH), exist_ok=True)
os.makedirs(os.path.dirname(TSN_FILE_PATH), exist_ok=True)

def read_csv(filepath: str, recordtype: RecordType) -> list:
    rows_buffer = []
    with open(filepath, "r") as csvfile:
        reader = csv.reader(csvfile)
        for row in reader:
            raw_datetime = row[0]
            raw_data = row[1]            
            parsed_datetime = datetime.datetime.fromisoformat(raw_datetime)
            rows_buffer.append([parsed_datetime, raw_data, recordtype])
    return rows_buffer

tsr_rows = []
tsn_rows = []

tsr_rows = read_csv(TSR_FILE_PATH, RecordType.TSR)
tsn_rows = read_csv(TSN_FILE_PATH, RecordType.TSN)
all_rows = tsr_rows + tsn_rows
sorted_rows = sorted(all_rows, key=lambda x: x[0])

# pretty_date = parsed_datetime.strftime('Started %H:%M on %d %b %Y')
html_entries = csv_to_timeline_entries(sorted_rows)
html_template = generate_html_template(html_entries)
html_template_to_file(html_template, HTML_OUTPUT_PATH)

webbrowser.open('file://'+os.path.realpath(HTML_OUTPUT_PATH))
print("Compiled the html report.")
