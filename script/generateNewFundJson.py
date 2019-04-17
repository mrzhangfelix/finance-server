#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import json
import traceback
import time
import codecs
import os
from utils.requests import get_html
from utils.time import get_week
from utils.fund import new_fund,new_fundconf,get_url_amount,get_fundconf


base_url = 'http://fundgz.1234567.com.cn/js/{}.js?rt={}'
sum = 0
gztime = ''
module_path = os.path.dirname(__file__)

def get_NewFund(fund,url,amount):
    try:
        res=get_html(url)
        res=res[8:-2]
        fundinfo=json.loads(res)
        amountNew=round(float(fundinfo['gszzl'])*amount/100+amount,2)
        yingli=round(float(fundinfo['gszzl'])*amount/100,2)
        dwjz=float(fundinfo['dwjz'])
        holdShare=round(amount/dwjz,2)
        # 估算值
        gsz=float(fundinfo['gsz'])
        week=get_week()
        fundnew=new_fund()
        fundnew['fundName'] = fundinfo['name']
        fundnew['fundcode'] =fund['fundcode']
        fundnew['add']=fund['add']
        buychange=int(fund['add'])+int(fund['amountChange'])
        sellchange=round(float(fund['shareChange'])*gsz,2)
        fundnew['fundamount'] = amountNew+buychange-sellchange
        fundnew['yingli'] = yingli
        fundnew['zhangfu'] = float(fundinfo['gszzl'])
        fundnew['dwjz'] = dwjz
        fundnew['holdShare'] = holdShare
        fundnew['amountNow'] = round(holdShare*gsz,2)
        fundnew['gusuanzhi'] = gsz
        fundnew['buyamount7']=fund['buyamount7']
        fundnew['buyshare7']=fund['buyshare7']
        fundnew['buyamount7'][week]=buychange
        fundnew['buyshare7'][week]=round(buychange/gsz,2)
        global gztime
        gztime=fundinfo['gztime']
        global sum
        sum+=yingli
    except BaseException as e:
        print('获取信息失败')
        print(str(traceback.format_exc()))
    return fundnew

def getfundconf():
    fundconf=get_fundconf()
    url_list,amountlist=get_url_amount(fundconf)
    # 获取基金数据
    fundconfnew=new_fundconf()
    for fund,url,amount in zip(fundconf['fundlist'],url_list,amountlist):
        fundnew=get_NewFund(fund,url,amount)
        fundconfnew['fundlist'].append(fundnew)
    fundconfnew['todayIncameSum'] = round(sum,2)
    fundconfnew['gztime'] = gztime[0:10]
    return fundconfnew

def main():
    fundconf=getfundconf()
    # 格式化json
    strRes= json.dumps(fundconf, indent=4, separators=(',', ':'), ensure_ascii=False)
    filename=time.strftime(module_path+"\\..\\history\\%Y-%m-%d.json", time.localtime())
    with codecs.open(filename, 'w' ,"utf-8") as f:
        f.write(str(strRes))
    print("成功生成"+filename+"配置文件")

if __name__ == '__main__':
    main()
