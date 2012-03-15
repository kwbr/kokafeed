from urlparse import urljoin
import urllib2
from bs4 import BeautifulSoup
import datetime
import PyRSS2Gen

def make_external(url):
    return urljoin("http://www.koka36.de", url)

def main():

    html = urllib2.urlopen('http://www.koka36.de/neu_im_vorverkauf.php').read()
    soup = BeautifulSoup(html)

    items = []

    for link in soup.find_all('a', { 'class' : 'tipps'}):

        title = link.get_text()

        if title:
            item = PyRSS2Gen.RSSItem(
                    title = link.get_text(),
                    link = make_external(link.get('href')),
                    description = link.get('onmouseover'),
                    guid = PyRSS2Gen.Guid(link.get('href')))

            items.append(item)

    rss = PyRSS2Gen.RSS2(
            title = "Neu im Vorverkauf",
            link = "http://www.koka36.de/",
            description = "Generated using bs4, PyRSS2Gen",
            lastBuildDate = datetime.datetime.utcnow(),
            items = items)

    rss.write_xml(open("neu.rss", "w"))

if __name__ == '__main__':
    main()
