import requests
from bs4 import BeautifulSoup
import re
from datetime import date
import json

#URL for Sample Surf Spot:
UrlBelmar =  "https://magicseaweed.com/Belmar-Surf-Report/3683/"

#Gets Today's date in format for Parsing
date_anchor = str(date.today().strftime("%A%d%m"))

#Function dictionary of swell, wind, direction
#url represents the spot, timestamp represents the
#def strike(url, timestamp):

# request to get info from url
r = requests.get(UrlBelmar)
#create the soup of html
soup = BeautifulSoup(r.content, "html5lib")


x = soup.find_all('tr', {'data-date-anchor': date_anchor})

# a list of swell size and period for
listofswell = []
listofperiod = []
listofsdirection = []
listofwdirection = []
listofwindspeed = []
#x = '<td data-original-title="ESE - 110°"></td>'

#testsoup = BeautifulSoup(x, 'html5lib')

#newnew = testsoup.find_all('td', {dat})
#print(newnew)

for itemone in x:
    listofswell.append(itemone.find_all('h4')[0].text)
    listofperiod.append(itemone.find_all('h4')[1].text)
    listofwindspeed.append(itemone.find('strong').text)
    #list of swell direction
    cols = itemone.find_all('td')
    for col in cols:
        if col.get('class') == ['text-center', 'msw-js-tooltip', 'background-gray-lighter']:
            listofsdirection.append(col.get('title'))
    #list of wind direction
        if col.get('class') == ['text-center', 'last', 'msw-js-tooltip', 'td-square', 'background-success']:
            listofwdirection.append(col.get('title'))

print(listofwindspeed)

#num = 0
#for item in listofswell:
    #new = item.split()
    #listofswell[num] = new[0]
    #num +=1
#print(listofswell)
