#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import json
import traceback
import requests
import time
import codecs
import os

base_url = 'http://img1.money.126.net/chart/hs/time/210x140/0000001.png?{$VERSION}'
base_url = 'http://img1.money.126.net/chart/hs/time/210x140/1399001.png?{$VERSION}'
base_url = 'http://img1.money.126.net/chart/hs/time/210x140/1399300.png?{$VERSION}'
# http://d1.biz.itc.cn/q/zs/001/000001/tline.png
indexInfolist={}
# 0:name 1：今开 2：昨收  3：现值  4：最高  5：最低  6：  7：  8：成交量（手） 9：成交额
def get_html(url):
    try:
        headers = {'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10.13; rv:60.0) Gecko/20100101 Firefox/60.0'}
        r=requests.get(url,timeout=30, headers = headers)
        r.raise_for_status()
        r.encoding='gbk'
        return r.text
    except:
        print('获取数据失败，请检查你的网络连接')
        print(str(traceback.format_exc()))
        return "ERROR"

def main(base_url):
    indexInfolist={}
    indexInfoStr=get_html(base_url)
    indexInfolistStr=indexInfoStr.split('\n')
    for indexStr in indexInfolistStr:
        key=indexStr[11:19]
        value=indexStr[21:-2].split(',')
        if key !='':
            indexInfolist[key]=value
    res=str(indexInfolist).replace('\'','\"')
    print(res)

if __name__ == '__main__':
    main(base_url)
