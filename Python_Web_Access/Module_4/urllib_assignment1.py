# Scraping Numbers from HTML using BeautifulSoup In this assignment you will write a Python program similar to http://www.py4e.com/code3/urllink2.py. The program will use urllib to read the HTML from the data files below, and parse the data, extracting numbers and compute the sum of the numbers in the file.

import urllib.request, urllib.parse, urllib.error
from bs4 import BeautifulSoup
import ssl

# Ignore SSL certificate errors
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

# URL to scrape
url = input('Enter - ')
html = urllib.request.urlopen(url, context=ctx).read()
soup = BeautifulSoup(html, 'html.parser')

# Initialize a running total
total = 0

# Retrieve all of the span tags
tags = soup.find_all('span')
for tag in tags:
    # Extract the text from each span tag and convert it to an integer
    number = int(tag.text)
    # Add the number to a running total
    total += number
# Print the total sum of the numbers found in the span tags
print(total)