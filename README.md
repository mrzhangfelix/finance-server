# finance-server

## 财务平台后端项目
  java+python+Springboot 

## 目前支持功能：

>1、基金配置文件数据的展示（时间，盈利，基金列表）

>2、基金配置文件的手动更新，自动获取前一个交易日的数据。

>3、基金列表中单个基金的信息修改（持有总值，定投，今日买入卖出）

>4、增加新的基金信息

>5、根据涨跌情况自动计算当前总收益和单个基金的情况。

>6、基金列表表格可排序，涨跌情况标记

## 预计完成的功能：

>1、导入导出基金列表（Excle）

>2、设置基金收益提醒（邮件）

基金配置字段：
{
>  "gztime":交易时间,
>  "todayIncameSum":今日收入总和,
>  "fundlist":[{
>>      "fundName":基金名称,
>>      "fundcode":基金编码,
>>      "add":定投金额,
>>			"zhangfu":涨幅,
>>			"fundamount":持有金额,
>>			"dwjz":单位净值,
>>			"gusuanzhi":估算值,
>>			"amountNow":现持有金额,
>>			"yingli":盈利金额,
>>			"amountChange":买入金额,
>>			"holdShare":持有份额,
>>			"shareChange":卖出份额,
>>			"buyamount7":{
>>>				"Monday":100,
>>>				"Thursday":100,
>>>				"Friday":100,
>>>				"Wednesday":100,
>>>				"Tuesday":100
>>			},
>>    "buyshare7":{
>>>				"Monday":124.21,
>>>				"Thursday":123.67,
>>>				"Friday":123.99,
>>>				"Wednesday":121.39,
>>>				"Tuesday":122.38
>>			},
>		}]
  }
