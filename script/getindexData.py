#!/usr/bin/env python3
# -*- coding: utf-8 -*-
from utils.requests import get_html

base_url = 'http://api.money.126.net/data/feed/1399001,1399300,0000001,1399006'
# http://api.money.126.net/data/feed/1399001,1399300,0000001,1399006,HSRANK_COUNT_SHA,HSRANK_COUNT_SZA,HSRANK_COUNT_SH3
indexInfolist={}

def main(base_url):
    indexInfoStr=get_html(base_url)
    print(indexInfoStr[21:-2])

if __name__ == '__main__':
    main(base_url)
