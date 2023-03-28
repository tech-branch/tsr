#!/usr/bin/env /usr/bin/python3

# Required parameters:
# @raycast.schemaVersion 1
# @raycast.title tsv
# @raycast.mode compact

# Optional parameters:
# @raycast.icon ⏰
# @raycast.packageName Timestamp Recorder HTML view

# Documentation:
# @raycast.description Compile your records into a timeline
# @raycast.author Tomasz Sobota
# @raycast.authorURL https://techbranch.net

import csv
import datetime
import os
import webbrowser


class RecordType:
    TSR = 1
    TSN = 2


class RecordSide:
    LEFT = "left"
    RIGHT = "right"


# ------------
#  PARAMETERS
# ------------
# modify to your preference

home_path = os.path.expanduser('~')
TSR_FILE_PATH = home_path + "/tsr/record.csv"
TSN_FILE_PATH = home_path + "/tsr/notes.csv"
HTML_OUTPUT_PATH = home_path + "/tsr/record.html"

CSS_ASSETS_PATH = "../assets/timeline.css"

DEFAULT_ENTRY_SIDE = RecordSide.LEFT

# ---------
#  Helpers
# ---------


# function assigning side to a record type
def get_timeline_side(record_type: RecordType):
    if record_type == RecordType.TSR:
        return RecordSide.LEFT
    if record_type == RecordType.TSN:
        return RecordSide.RIGHT
    return DEFAULT_ENTRY_SIDE


def csv_to_timeline_entries(trows: list):
    containers = []
    for row in trows:

        ts_side = get_timeline_side(row[2])
        pretty_date = row[0].strftime('%H:%M on %d %b %Y')

        html_container = f'<div class="container {ts_side}">\n<div class="content">\n'
        html_container += f'<h2>{row[1]}</h2>\n'
        html_container += f'<p>{pretty_date}</p>\n'
        html_container += '</div>\n</div>\n'

        containers.append(html_container)
    # return containers as a single string with reversed order
    return "".join(containers[::-1])


def generate_html_template(embedded_html: str, stylesheet: str):
    css = ""
    if stylesheet:
        css = f"""
        <style>
        {stylesheet}
        </style>
        """

    html_template = f"""<!DOCTYPE html>
    <html>
    <head>
    {css}
    </head>
    <body>

    <div class="timeline">
        {embedded_html}
    </div>

    </body>
    </html>"""
    return html_template


def html_template_to_file(html_template: str, file_path: str):
    """Save html template to file"""
    fp = file_path
    if file_path is None:
        fp = HTML_OUTPUT_PATH

    with open(fp, "w") as f:
        f.write(html_template)


def read_csv(filepath: str, recordtype: RecordType) -> list:
    rows_buffer = []
    with open(filepath, "r") as csvfile:
        reader = csv.reader(csvfile)
        for row in reader:

            if len(row) == 0:
                # omit empty rows
                continue

            raw_datetime = row[0]
            raw_data = row[1]
            parsed_datetime = datetime.datetime.fromisoformat(raw_datetime)
            rows_buffer.append([parsed_datetime, raw_data, recordtype])
    return rows_buffer


def read_file_to_str(filepath):
    with open(filepath, 'r') as file:
        return file.read()


# ------
#  Main
# ------

# make sure directories exist
os.makedirs(os.path.dirname(TSR_FILE_PATH), exist_ok=True)
os.makedirs(os.path.dirname(TSN_FILE_PATH), exist_ok=True)

tsr_rows = []
tsn_rows = []

tsr_rows = read_csv(TSR_FILE_PATH, RecordType.TSR)
tsn_rows = read_csv(TSN_FILE_PATH, RecordType.TSN)
all_rows = tsr_rows + tsn_rows
sorted_rows = sorted(all_rows, key=lambda x: x[0])

css_stylesheet = read_file_to_str(CSS_ASSETS_PATH)
html_entries = csv_to_timeline_entries(sorted_rows)
html_template = generate_html_template(html_entries, css_stylesheet)
_ = html_template_to_file(html_template, HTML_OUTPUT_PATH)

webbrowser.open('file://' + os.path.realpath(HTML_OUTPUT_PATH))
print("Compiled the html report.")
