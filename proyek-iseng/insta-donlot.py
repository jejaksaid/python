"""
Instagram Photo Downloader
"""

from sys import argv
import urllib
from bs4 import BeautifulSoup
import datetime
def ShowHelp():
    print 'Insta Image Downloader'
    print ''
    print 'Usage:'
    print 'insta.py [OPTION] [URL] '
    print ''
    print 'Options:'
    print