# -*- coding：utf-8 -*-

import feedparser
import re


def getwordcounts(url):
    d = feedparser.parse(url)
    wc = {}

    if len(d.entries) != 0:
        for e in d.entries:
            if 'summary' in e:
                summary = e.summary
            else:
                summary = e.description

            words = getwords(e.title + '' + summary)
            for word in words:
                wc.setdefault(word,0)
                wc[word] += 1

        return d.feed.title, wc
    else:
        return None, None


def getwords(html):
    txt = re.compile(r'<[^>]+>]').sub('',html)

    words = re.compile(r'[^A-Z^a-z]+').split(txt)

    return [word.lower() for word in words if word != '']


apcount = {}
wordcounts = {}

fp = open('feedlist.txt')
feedlist = [line for line in fp.readlines()]
fp.close()

for feedurl in feedlist:
    title, wc = getwordcounts(feedurl)
    if title is not None:
        wordcounts[title] = wc
        for word, count in wc.items():
            apcount.setdefault(word,0)
            if count>1:
                apcount[word]+=1

print(wordcounts)