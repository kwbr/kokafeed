PWD		:= $(shell pwd)
RSSFILE = feed.rss

build:
	./kokafeed.py > ${RSSFILE}

publish: build
	scp ${RSSFILE} u8767@www.glorybox.de:de.glorybox.www/feeds

clean:
	-rm ${RSSFILE}

.PHONY: html clean

