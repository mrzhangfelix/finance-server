import os
import codecs
import json
from .time import current_milli_time

base_url='http://fundgz.1234567.com.cn/js/{}.js?rt={}'

def new_fund():
    fund={}
    fund['fundName'] = ''
    fund['fundcode'] = ''
    fund['add']=0
    fund['amountChange']=0
    fund['shareChange']=0
    fund['amountChange'] = 0
    fund['shareChange'] = 0
    fund['fundamount'] = 0
    fund['yingli'] = 0
    fund['zhangfu'] = 0
    fund['dwjz'] = 0
    fund['holdShare'] = 0
    fund['amountNow'] = 0
    fund['gusuanzhi'] = 0
    fund['buyamount7']={}
    fund['buyshare7']={}
    return fund

def new_fundconf():
    fundconf={}
    fundconf['gztime']=''
    fundconf['todayIncameSum']=''
    fundconf['fundlist']=[]
    return fundconf

# 获取fund.json对象字典
def get_fundconf():
    module_path = os.path.dirname(__file__)
    with codecs.open(module_path+'\\..\\'+'fund.json', 'r', 'utf-8') as f:
        fundJson=f.read()
        fundconf=json.loads(fundJson)
    return fundconf

# 根据fundconf得到请求的url，和持有金额列表
def get_url_amount(fundconf):
    codelist=[]
    amountlist=[]
    url_list=[]
    for fund in fundconf['fundlist']:
        codelist.append(fund['fundcode'])
        amountlist.append(float(fund['fundamount']))
    for i in codelist:
        url_list.append(base_url.format(i,current_milli_time()))
    return url_list,amountlist
