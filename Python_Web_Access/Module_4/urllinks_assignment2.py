# In this assignment you will write a Python program that expands on http://www.py4e.com/code3/urllinks.py. The program will use urllib to read the HTML from the data files below, extract the href= vaues from the anchor tags, scan for a tag that is in a particular position relative to the first name in the list, follow that link and repeat the process a number of times and report the last name you find.

import urllib.request, urllib.parse, urllib.error
from bs4 import BeautifulSoup
import ssl

# Ignore SSL certificate errors
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

# Fetch Input from the user
url = input('Enter URL - ')
count = int(input('Enter count - '))
position = int(input('Enter position - '))

# Initialize a list to store names
names = []

# Loop through the specified number of times
while count > 0:
    # Read the HTML from the URL
    print ('Retrieving', url)   
    html = urllib.request.urlopen(url, context=ctx).read()
    soup = BeautifulSoup(html, 'html.parser')

    # Retrieve all of the anchor tags
    tags = soup('a')
    # grab the name at the specified position
    name = tags[position - 1].string
    # Add the name to the list
    names.append(name)
    # Update the URL to the next link
    url = tags[position - 1]['href']
    # adjust the count
    count -= 1
  
# Print the last name found
print(names[-1])
