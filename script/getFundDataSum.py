#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import datetime
import json
import traceback
import time
import codecs
import os
import threading
from utils.requests import get_html

current_milli_time = lambda: int(round(time.time() * 1000))
module_path = os.path.dirname(__file__)

base_url = 'http://fundgz.1234567.com.cn/js/{}.js?rt={}'
sum = 0
gztime = ''

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
    # print(timer.getName())
    now = datetime.datetime.now()
    print('hour:'+str(now.hour)+',minute:'+str(now.minute))
    if (now.hour==11 and now.minute==30):
        print('中午休息90分钟！')
        time.sleep(60*90)
    if (now.hour == 15 and now.minute==0):
        print('结束程序')
        os._exit(0)
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
    timer = threading.Timer(61, main)
    timer.start()

if __name__ == '__main__':
    timer = threading.Timer(2, main)
    timer.start()
