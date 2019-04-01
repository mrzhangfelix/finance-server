#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import traceback
import requests

indexlist=['0000001','1399001','1399300','1399006']
base_url = 'http://img1.money.126.net/chart/hs/time/540x360/'
# base_url = 'http://img1.money.126.net/chart/hs/time/210x140/1399001.png?{$VERSION}'
# base_url = 'http://img1.money.126.net/chart/hs/time/210x140/1399300.png?{$VERSION}'
# # http://d1.biz.itc.cn/q/zs/001/000001/tline.png
# http://img1.money.126.net/chart/hs/time/540x360/0000001.png

def get_png(url):
    try:
        headers = {'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10.13; rv:60.0) Gecko/20100101 Firefox/60.0'}
        r=requests.get(url,timeout=30, headers = headers)
        r.raise_for_status()
        return r.content
    except:
        print('获取数据失败，请检查你的网络连接')
        print(str(traceback.format_exc()))
        return "ERROR"

def main(base_url):
    for index in indexlist:
        filename='data\\'+index+'.png'
        url=base_url+index+'.png'
        open(filename, 'wb').write(get_png(url))

if __name__ == '__main__':
    main(base_url)
