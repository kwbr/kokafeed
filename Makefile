PWD		:= $(shell pwd)

build:
	./kokafeed.py

publish: build
	scp neu.rss u8767@www.glorybox.de:de.glorybox.www/feeds

clean:
	-rm neu.rss

.PHONY: html clean

