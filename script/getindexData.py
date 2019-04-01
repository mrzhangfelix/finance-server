#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import json
import traceback
import requests
import time
import codecs
import os

base_url = 'http://api.money.126.net/data/feed/1399001,1399300,0000001,1399006'
# http://api.money.126.net/data/feed/1399001,1399300,0000001,1399006,HSRANK_COUNT_SHA,HSRANK_COUNT_SZA,HSRANK_COUNT_SH3
indexInfolist={}
def get_html(url):
    try:
        headers = {'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10.13; rv:60.0) Gecko/20100101 Firefox/60.0'}
        r=requests.get(url,timeout=30, headers = headers)
        r.raise_for_status()
        r.encoding='utf-8'
        return r.text
    except:
        print('获取数据失败，请检查你的网络连接')
        print(str(traceback.format_exc()))
        return "ERROR"

def main(base_url):
    indexInfoStr=get_html(base_url)
    print(indexInfoStr[21:-2])

if __name__ == '__main__':
    main(base_url)
