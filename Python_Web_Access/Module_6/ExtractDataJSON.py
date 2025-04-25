# The program will prompt for a URL, read the JSON data from that URL using urllib and then parse and extract the comment counts from the JSON data, compute the sum of the numbers in the file and enter the sum below:

import json
import urllib.request, urllib.parse, urllib.error
import xml.etree.ElementTree as ET

# Prompt for a URL
url = input('Enter location: ') 

# Open the URL and read the data
address = urllib.request.urlopen(url)
data = address.read()

# Display URL and number of characters retrieved
print('Retrieving', url)
print('Retrieved', len(data), 'characters')

# Load the JSON data
info = json.loads(data)
info = info['comments']

# Print the number of comments
print('Count:', len(info))

# initialize total to 0
total = 0

# Loop through the comments and sum the numbers
for item in info:
    total = total + int(item["count"])

# Print the sum of numbers
print("Sum: ", total)