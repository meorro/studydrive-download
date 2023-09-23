# NOTE: The "requests" module is required for this script to work.
# Install it with: pip3 install requests
#
# Author: meorro
#
# Usage: python3 studydrive-download.py
#        python3 studydrive-download.py --name="writeYourPDFNameHere.pdf"
####################################################################################################

import sys
import requests

# Studydrive document URL
studydrive_url = input("Enter the Studydrive document URL: ")

# get the source of the URL
studydrive_url_source = requests.get(studydrive_url).text

# search for the key "file_preview" in the source
# and extract the value of the key
pdf_url = studydrive_url_source.split('"file_preview":"')[1].split('","')[0]

# clean up the PDF URL
pdf_url = pdf_url.replace("\\", "")

# replace "teaser" PDF URL with "original" PDF URL
pdf_url = pdf_url.replace("teaser", "original")

# if the program is invoked with the --name flag,
# use the name given by the user
if len(sys.argv) > 1 and sys.argv[1].startswith("--name="):
    pdf_name = sys.argv[1].split("--name=")[1]

    # if the user has not entered the ".pdf" extension, add it
    if ".pdf" not in pdf_name:
        pdf_name += ".pdf"

# otherwise, use the PDF file name given by the author
else:
    # search for the key "filename" in the source
    # and extract the value of the key
    pdf_name = studydrive_url_source.split('"filename":"')[1].split('","')[0]

# download the PDF and save it to the current folder
pdf_file = requests.get(pdf_url)
with open(pdf_name, "wb") as f:
   f.write(pdf_file.content)

print("Download complete!")