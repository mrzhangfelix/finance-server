#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import datetime
import json
import traceback
import requests
import time
import codecs
import os
import threading

current_milli_time = lambda: int(round(time.time() * 1000))
module_path = os.path.dirname(__file__)

base_url = 'http://fundgz.1234567.com.cn/js/{}.js?rt={}'
sum = 0
gztime = ''

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

def cal_sum(url,amount):
    try:
        res=get_html(url)
        res=res[8:-2]
        fundinfo=json.loads(res)
        yingli=float(fundinfo['gszzl'])*amount/100
        yingli=round(yingli,2)
        global sum,gztime
        gztime=fundinfo['gztime']
        sum+=yingli
    except BaseException as e:
        print('获取信息失败')
        print(str(traceback.format_exc()))

def main():
    global timer
    now = datetime.datetime.now()
    if (now.hour==11 and now.minute==31)or(now.hour==15 and now.minute==1):
        timer.cancel()
    codelist=[]
    amountlist=[]
    url_list=[]
    with codecs.open(module_path+'\\'+'fund.json', 'r', 'utf-8') as f:
        fundJson=f.read()
        fundconf=json.loads(fundJson)
    for fund in fundconf['fundlist']:
        codelist.append(fund['fundcode'])
        amountlist.append(float(fund['fundamount']))
    for i in codelist:
        url_list.append(base_url.format(i,current_milli_time()))
    global sum
    sum=0
    for url,amount in zip(url_list,amountlist):
        cal_sum(url,amount)
    fileName=module_path+"\\..\\data\\yingliList\\"+gztime[:10]+".txt"
    # print(fileName)
    with codecs.open(fileName, 'a' ,"utf-8") as f:
        f.write(gztime+','+str(round(sum,2))+';\n')
    print(gztime+','+str(round(sum,2))+';')
    timer = threading.Timer(60, main)
    timer.start()

if __name__ == '__main__':
    timer = threading.Timer(2, main)
    timer.start()
