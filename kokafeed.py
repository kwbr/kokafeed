#!/usr/bin/env python
import urlparse
import urllib2
import bs4
import datetime
import PyRSS2Gen
import re

def make_external(url):
    return urlparse.urljoin("http://www.koka36.de", url)

def main():

    html = urllib2.urlopen('http://www.koka36.de/neu_im_vorverkauf.php').read()
    soup = bs4.BeautifulSoup(html)

    items = []

    for link in soup.find_all('a', { 'class' : 'tipps'}):

        title = link.get_text()

        if title:
            item = PyRSS2Gen.RSSItem(
                    title = link.get_text(),
                    link = make_external(link.get('href')),
                    description = re.sub(r'return overlib\(\'([^)]*)\'\);', "\\1", link.get('onmouseover') or ''),
                    guid = PyRSS2Gen.Guid(link.get('href')))

            items.append(item)

    rss = PyRSS2Gen.RSS2(
            title = "Neu im Vorverkauf",
            link = "http://www.koka36.de/",
            description = "Generated using bs4, PyRSS2Gen",
            lastBuildDate = datetime.datetime.utcnow(),
            items = items)

    print rss.to_xml()

if __name__ == '__main__':
    main()
