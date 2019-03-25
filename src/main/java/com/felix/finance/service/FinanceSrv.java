package com.felix.finance.service;

import com.alibaba.fastjson.JSON;
import com.alibaba.fastjson.JSONArray;
import com.alibaba.fastjson.JSONObject;
import com.felix.finance.entity.FundInfo;
import com.felix.finance.entity.FundJson;
import com.felix.finance.util.FileUtils;
import org.springframework.stereotype.Service;

import java.io.File;
import java.io.IOException;
import java.util.Date;
import java.util.List;

@Service
public class FinanceSrv {
    private static final String separator =File.separator;

//    使用JSONObject的方式处理字符串，此方法要比javabean的方式更快，不过javabean的方式处理很方便
    public String changeJsonByCode(String fundcode,String add,String amountChange,String fundamount){
        long startTime=System.currentTimeMillis();
        String res="失败";
        File directory = new File("");
        String filePath= directory.getAbsolutePath()+separator+"script"+separator+"fund.json";
        String str=FileUtils.getfileContent(filePath);
        JSONObject obj = JSON.parseObject(str);
        JSONArray fundlist=(JSONArray)obj.get("fundlist");
        for(int i=0;i<fundlist.size();i++){
            JSONObject fund=(JSONObject) fundlist.get(i);
            if(fund.get("fundcode").equals(fundcode)){
                fund.put("fundamount",fundamount);
                fund.put("add",add);
                fund.put("amountChange",amountChange);
            }
        }
        FileUtils.writeStringtoFile(obj.toString(),filePath);
        res="成功";
        long endTime=System.currentTimeMillis();
        System.out.println("JavaObject方式程序运行时间： "+(endTime-startTime)+"ms");
        return res;
    }

    public String addJsonData(String fundcode,
                              String fundamount){
        String res="失败";
        File directory = new File("");
        String filePath= directory.getAbsolutePath()+separator+"script"+separator+"fund.json";
        String str=FileUtils.getfileContent(filePath);
        JSONObject obj = JSON.parseObject(str);
        JSONArray fundlist=(JSONArray)obj.get("fundlist");
        JSONObject newfund=new JSONObject();
        newfund.put("fundamount",fundamount);
        newfund.put("fundcode",fundcode);
        fundlist.add(newfund);
        FileUtils.writeStringtoFile(obj.toString(),filePath);
        res="成功";
        return res;
    }

    public String updatefundjson(String lastTradingDate){
        String res="失败";
        Date now = new Date();
        //判断配置文件是不是最新
        File directory = new File("");
        String filePath= directory.getAbsolutePath()+separator+"script"+separator+"fund.json";
        String curJson=FileUtils.getfileContent(filePath);
        JSONObject obj = JSON.parseObject(curJson);
        String gztime=obj.get("gztime").toString();
        if(lastTradingDate.equals(gztime)){
            res="当前配置已经是最新"+lastTradingDate+"的配置！无需更新";
            return res;
        }else{
            String newfilePath= directory.getAbsolutePath()+separator+"history"+separator+lastTradingDate+".json";
            File source=new File(newfilePath);
            File dest=new File(filePath);
            try {
                FileUtils.copyFileUsingFileStreams(source,dest);
            } catch (IOException e) {
                e.printStackTrace();
            }
            res="成功更新配置为 上一个交易日："+lastTradingDate+"时间的配置！";
            return res;
        }
    }
}
