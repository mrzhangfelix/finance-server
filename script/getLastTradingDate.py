#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import json
import traceback
import requests
import time


current_milli_time = lambda: int(round(time.time() * 1000))
base_url = 'http://fundgz.1234567.com.cn/js/161725.js?rt='+str(current_milli_time())

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
    res=get_html(base_url)
    res=res[8:-2]
    fundinfo=json.loads(res)
    gztime=fundinfo['gztime']
    jzrq=fundinfo['jzrq']
    today=time.strftime("%Y-%m-%d", time.localtime())
    if today == gztime[0:10]  :
        print(jzrq)
    else:
        print(gztime[0:10])

if __name__ == '__main__':
    main(base_url)
