#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import json
import traceback
import codecs
import os
from utils.requests import get_html
from utils.time import current_milli_time,get_week

base_url = 'http://fundgz.1234567.com.cn/js/{}.js?rt={}'
sum = 0
gztime = ''

def get_NewAmount(url,amount):
    try:
        res=get_html(url)
        res=res[8:-2]
        fundinfo=json.loads(res)
        amountNew=float(fundinfo['gszzl'])*amount/100+amount
        amountNew=round(amountNew,2)
        yingli=float(fundinfo['gszzl'])*amount/100
        yingli=round(yingli,2)
        zhangfu=float(fundinfo['gszzl'])
        name=fundinfo['name']
        # 单位净值
        dwjz=float(fundinfo['dwjz'])
        holdShare=round(amount/dwjz,2)
        # 估算值
        gsz=float(fundinfo['gsz'])
        amountNow=round(holdShare*gsz,2)
        global gztime
        # 估值时间
        gztime=fundinfo['gztime']
        global sum
        sum+=yingli
    except BaseException as e:
        print('获取信息失败')
        print(str(traceback.format_exc()))
    return amountNew,yingli,zhangfu,name,dwjz,holdShare,amountNow,gsz

def getfundconf():
    codelist=[]
    amountlist=[]
    url_list=[]
    amountNewlist=[]
    yingliList=[]
    zhangfuList=[]
    namelist=[]
    dwjzlist=[]
    holdSharelist=[]
    amountNowlist=[]
    gszlist=[]
    module_path = os.path.dirname(__file__)
    with codecs.open(module_path+'\\'+'fund.json', 'r', 'utf-8') as f:
        fundJson=f.read()
        fundconf=json.loads(fundJson)
    for fund in fundconf['fundlist']:
        codelist.append(fund['fundcode'])
        amountlist.append(float(fund['fundamount']))
    for i in codelist:
        url_list.append(base_url.format(i,current_milli_time()))
    # 获取基金数据
    for url,amount in zip(url_list,amountlist):
        amountNew,yingli,zhangfu,name,dwjz,holdShare,amountNow,gsz=get_NewAmount(url,amount)
        amountNewlist.append(amountNew)
        yingliList.append(yingli)
        zhangfuList.append(zhangfu)
        namelist.append(name)
        dwjzlist.append(dwjz)
        holdSharelist.append(holdShare)
        amountNowlist.append(amountNow)
        gszlist.append(gsz)
    # 构造配置文件
    for fund,amountNew,yingli,zhangfu,name,dwjz,holdShare,amountNow,gsz in zip(fundconf['fundlist'],amountNewlist,yingliList,zhangfuList,namelist,dwjzlist,holdSharelist,amountNowlist,gszlist):
        fund['fundamount'] = amountNew
        fund['yingli'] = yingli
        fund['zhangfu'] = zhangfu
        fund['fundName'] = name
        fund['dwjz'] = dwjz
        fund['holdShare'] = holdShare
        fund['amountNow'] = amountNow
        fund['gusuanzhi'] = gsz
    fundconf['todayIncameSum'] = round(sum,2)
    fundconf['gztime'] = gztime[0:10]
    return fundconf

def main():
    fundconf=getfundconf();
    strRes=str(fundconf).replace("'",'"')
    print(str(strRes))

if __name__ == '__main__':
    main()
