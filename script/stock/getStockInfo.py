#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import json
import traceback
import time
import codecs
import os
from myrequests import get_html

base_url = 'http://sqt.gtimg.cn/utf8/q={}'
module_path = os.path.dirname(__file__)

def get_stockInfo(url):
    try:
        res=get_html(url)
        start = res.index('"')
        end = res.index('"',start+1)
        res=res[start+1:end]
        res=res.split("~")
    except BaseException as e:
        print('获取信息失败')
        print(str(traceback.format_exc()))
    return res

def getfundconf():
    code_list = []
    url_list = []
    stockInfoList = []
    # module_path = os.path.dirname(__file__)
    with codecs.open(module_path+'\\'+'stock.json', 'r', 'utf-8') as f:
        stockJson=f.read()
        stockconf=json.loads(stockJson)
    for stock in stockconf['stocklist']:
        code_list.append(stock)
    for i in code_list:
        url_list.append(base_url.format(i))
    # 获取基金数据
    for url in url_list:
        stockInfo=get_stockInfo(url)
        stockInfoList.append(stockInfo)
    return str(stockInfoList)

def main():
    strRes=getfundconf()
    # 格式化json
    filename=time.strftime(module_path+"\\%Y-%m-%dstock.json", time.localtime())
    with codecs.open(filename, 'w' ,"utf-8") as f:
        f.write(str(strRes))
    print("成功生成"+filename+"配置文件")

if __name__ == '__main__':
    main()
