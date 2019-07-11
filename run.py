#!/usr/bin/env python3
import requests
from bs4 import BeautifulSoup

headers = {'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10.9; rv:45.0) Gecko/20100101 Firefox/45.0'}

#url = 'https://vceguide.com/lpi/101-400-lpi-level-1-exam-101-junior-level-linux-certification-part-1-of-2/' # 101-400
#url = 'https://vceguide.com/lpi/101-400-lpi-level-1-exam-101-junior-level-linux-certification-part-1-of-2-v2/' # 101-400v2
url = 'https://vceguide.com/lpi/102-400-lpi-level-1-exam-102-junior-level-linux-certification-part-2-of-2/' # 102-400

data = requests.get(url, headers = headers)
html = BeautifulSoup(data.text, 'html.parser')
all_links = html.find_all('div', attrs={'class': 'wrap_page'})

allurl = {}
for al in all_links:
    for a in al.find_all('a'):
        allurl[a.text] = a['href']

for q, url in allurl.items():
    data = requests.get(url, headers = headers)

    # parse the html using beautiful soup and store in variable `soup`
    html = BeautifulSoup(data.text, 'html.parser')

    content = html.find('div', attrs={'class': 'entry-content'})
    answer =  ( content.find('div', attrs={'class': 'sh-content pressrelease-content sh-hide'} ).find('strong') )

    [s.extract() for s in content('div')] # del all tags <dev .* >.*</dev> in content

    var = content.find_all('strong')

    [s.extract() for s in content('strong')] # del all tags <strong>.*</strong> in content
    content = content.find('p')
    [s.extract() for s in content('br')] # del all tags <strong>.*</strong> in content

    if "SIMULATION" in content.text:
        print ( "[",q,"]\n", content.text.strip(), "\n\n\n\n\n\n\n\n\n\n\n")
        for v in var:print ( v.text )
        print (answer.text, "\n" )
    else:
        print ( "[",q,"]\n", content.text.strip())
        for v in var:print ( v.text )
        print ("\n\n\n\n\n\n\n\n\n\n\n", answer.text, "\n" )
