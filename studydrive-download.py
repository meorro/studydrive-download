# NOTE: The "requests" module is required for this script to work.
# Install it with: pip3 install requests
#
# Author: meorro
#
# Usage: python3 studydrive-download.py
#
# Result: The PDF will be downloaded to the current folder with your chosen name.
####################################################################################################

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

# enter download name for the PDF
pdf_name = input("How would you like to name the PDF? (e.g. studydrive.pdf): ")

# if the user has not entered the ".pdf" extension, add it
if ".pdf" not in pdf_name:
    pdf_name += ".pdf"

# download the PDF and save it to the current folder
pdf_file = requests.get(pdf_url)
with open(pdf_name, "wb") as f:
   f.write(pdf_file.content)

print("Download complete!")