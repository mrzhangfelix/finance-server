#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import json
import traceback
import requests
import time
from utils.requests import get_html

current_milli_time = lambda: int(round(time.time() * 1000))
base_url = 'http://fundgz.1234567.com.cn/js/161725.js?rt='+str(current_milli_time())


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
