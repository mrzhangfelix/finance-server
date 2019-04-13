#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import json
import traceback
import time
import codecs
import os
from utils.requests import get_html
from utils.time import current_milli_time,get_week

base_url = 'http://fundgz.1234567.com.cn/js/{}.js?rt={}'
sum = 0
gztime = ''
module_path = os.path.dirname(__file__)

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
        if not ('add') in fund:
            fund['add']=0
        if not ('amountChange') in fund:
            fund['amountChange']=0
        if not ('shareChange') in fund:
            fund['shareChange']=0
        if not ('buyamount7') in fund:
            fund['buyamount7']={}
        if not ('buyshare7') in fund:
            fund['buyshare7']={}
        buychange=int(fund['add'])+int(fund['amountChange']);
        sellchange=round(float(fund['shareChange'])*gsz,2)
        fund['fundamount'] = amountNew+buychange-sellchange
        week=get_week()
        fund['buyamount7'][week]=buychange
        fund['buyshare7'][week]=round(buychange/gsz,2)
        fund['amountChange'] = 0
        fund['shareChange'] = 0
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
    fundconf=getfundconf()
    # 格式化json
    strRes=str(fundconf).replace("'",'"')
    strRes=strRes.replace(",",",\n\t")
    strRes=strRes.replace("[","[\n\t")
    strRes=strRes.replace("{","{\n\t")
    strRes=strRes.replace("}","\n}")
    filename=time.strftime(module_path+"\\..\\history\\%Y-%m-%d.json", time.localtime())
    with codecs.open(filename, 'w' ,"utf-8") as f:
        f.write(str(strRes))
    print("成功生成"+filename+"配置文件")

if __name__ == '__main__':
    main()
