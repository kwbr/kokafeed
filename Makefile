PWD		:= $(shell pwd)

build:
	kokafeed.py

publish: neu.rss
	scp neu.rss u8767@www.glorybox.de:de.glorybox.www/feeds

clean:
	-rm neu.rss

.PHONY: html clean

