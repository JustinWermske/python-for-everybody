import urllib.request, urllib.parse
import json, ssl

# Heavily rate limited proxy of https://www.geoapify.com/ api
serviceurl = 'https://py4e-data.dr-chuck.net/opengeo?'

# Ignore SSL certificate errors
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

while True:
    # Prompt for a location
    address = input('Enter location: ')
    if len(address) < 1: break

    # Geocoding API URL
    address = address.strip()
    parms = dict()
    parms['q'] = address
    url = serviceurl + urllib.parse.urlencode(parms)

    # Display URL and number of characters retrieved
    print('Retrieving', url)
    uh = urllib.request.urlopen(url, context=ctx)
    data = uh.read().decode()
    print('Retrieved', len(data), 'characters')

    # Load the JSON data
    try:
        js = json.loads(data)
    except:
        js = None

    # Check if JSON data is valid
    if not js or 'features' not in js:
        print('==== Download error ===')
        print(data)
        break

    if len(js['features']) == 0:
        print('==== Object not found ====')
        print(data)
        break
    
    # Retrieve and print the plus code
    pluscode = js['features'][0]['properties']['plus_code']
    print("Plus code", pluscode)