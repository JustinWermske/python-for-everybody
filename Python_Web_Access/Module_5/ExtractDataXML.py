# The program will prompt for a URL, read the XML data from that URL using urllib and then parse and extract the comment counts from the XML data, compute the sum of the numbers in the file.

import urllib.request, urllib.parse, urllib.error
import xml.etree.ElementTree as ET

# Prompt for a URL
url = input('Enter location: ') 

# Open the URL and read the data
print('Retrieving', url)
uh = urllib.request.urlopen(url)
data = uh.read()

# Print the number of characters retrieved
print('Retrieved',len(data),'characters')

# Extract the comment counts
tree = ET.fromstring(data)
counts = tree.findall('.//count')
print('Count:', len(counts))

# Compute the sum of the counts
accum = 0
for count in counts:
    accum += int(count.text)
print('Sum:', accum)