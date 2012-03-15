PWD		:= $(shell pwd)

build:
	python feed.py

publish: neu.rss
	scp neu.rss u8767@www.glorybox.de:de.glorybox.www/feeds

clean:
	-rm neu.rss

.PHONY: html clean

