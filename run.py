#!/usr/bin/env python3
import requests
from bs4 import BeautifulSoup
import re

headers = {'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10.9; rv:45.0) Gecko/20100101 Firefox/45.0'}
#url = 'https://vceguide.com/lpi/101-400-lpi-level-1-exam-101-junior-level-linux-certification-part-1-of-2-v2/'
url = 'https://vceguide.com/which-sysv-init-configuration-file-is-commonly-used-to-set-the-default-run-level/'
data = requests.get(url, headers = headers)

# parse the html using beautiful soup and store in variable `soup`
html = BeautifulSoup(data.text, 'html.parser')

content = html.find('div', attrs={'class': 'entry-content'})

answer =  ( content.find('div', attrs={'class': 'sh-content pressrelease-content sh-hide'} ).find('strong') )
var =  ( content.find('strong') )


[s.extract() for s in content('div')] # del all tags <dev .* >.*</dev> in content
[s.extract() for s in content('strong')] # del all tags <dev .* >.*</dev> in content

if str.find(content.text, "SIMULATION"):
    print ( content.text, "\n\n\n\n\n\n\n\n", var.text, "\n", answer.text, "\n\n" )
else:
    print ( content.text, "\n", var.text, "\n\n\n\n\n\n\n\n", answer.text, "\n\n" )

