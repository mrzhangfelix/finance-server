#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import json
import traceback
import requests
import time
import codecs
import os

current_milli_time = lambda: int(round(time.time() * 1000))

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


def get_NewAmount(url,amount):
    try:
        res=get_html(url)
        res=res[8:-2]
        fundinfo=json.loads(res)
        amountNew=float(fundinfo['gszzl'])*amount/100+amount
        amountNew=round(amountNew,2)
        yingli=float(fundinfo['gszzl'])*amount/100
        yingli=round(yingli,2)
        zhangfu=fundinfo['gszzl']+'%'
        name=fundinfo['name']
        global gztime
        gztime=fundinfo['gztime']
        global sum
        sum+=yingli
    except BaseException as e:
        print('获取信息失败')
        print(str(traceback.format_exc()))
    return amountNew,yingli,zhangfu,name



def main(base_url):
    codelist=[]
    amountlist=[]
    url_list=[]
    amountNewlist=[]
    yingliList=[]
    zhangfuList=[]
    namelist=[]
    module_path = os.path.dirname(__file__)
    with codecs.open(module_path+'\\'+'fund.json', 'r', 'utf-8') as f:
        fundJson=f.read()
        fundconf=json.loads(fundJson)
    for fund in fundconf['fundlist']:
        codelist.append(fund['fundcode'])
        amountlist.append(float(fund['fundamount']))
    for i in codelist:
        url_list.append(base_url.format(i,current_milli_time()))
    for url,amount in zip(url_list,amountlist):
        amountNew,yingli,zhangfu,name=get_NewAmount(url,amount)
        amountNewlist.append(amountNew)
        yingliList.append(yingli)
        zhangfuList.append(zhangfu)
        namelist.append(name)
    for fund,amountNew,yingli,zhangfu,name in zip(fundconf['fundlist'],amountNewlist,yingliList,zhangfuList,namelist):
        fund['fundamount'] = amountNew + int(fund['add']) + int(fund['amountChange'])
        fund['amountChange'] = 0
        fund['yingli'] = yingli
        fund['zhangfu'] = zhangfu
        fund['fundName'] = name
    fundconf['todayIncameSum'] = round(sum,2)
    fundconf['gztime'] = gztime[0:10]
    strRes=str(fundconf).replace("'",'"')
    strRes=strRes.replace(",",",\n\t")
    strRes=strRes.replace("[","[\n\t")
    strRes=strRes.replace("{","{\n\t")
    strRes=strRes.replace("}","\n}")
    filename=time.strftime("history\\%Y-%m-%d.json", time.localtime())
    with codecs.open(filename, 'w' ,"utf-8") as f:
        f.write(str(strRes))
    print(str(strRes))

if __name__ == '__main__':
    main(base_url)
