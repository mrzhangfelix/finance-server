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
public class FinanceBeanSrv {
    private static final String separator =File.separator;

//使用javabean的方式处理json字符串
    public String changeJsonByCode(String fundcode,String add,String amountChange,String fundamount){
        long startTime=System.currentTimeMillis();
        String res="失败";
        String filePath=FileUtils.getfilePath("script","fund.json");
        String str=FileUtils.getfileContent(filePath).replaceAll("\"","\'");
        FundJson fundJson=(FundJson)JSONObject.parseObject(str, FundJson.class);
        List<FundInfo> fundlist=fundJson.getFundlist();
        for(int i=0;i<fundlist.size();i++){
            FundInfo fund=fundlist.get(i);
            if(fund.getFundcode().equals(fundcode)){
                fund.setFundamount(fundamount);
                fund.setAdd(add);
                fund.setAmountChange(amountChange);
            }
        }
        String jsonStr=JSONObject.toJSONString(fundJson);
        FileUtils.writeStringtoFile(jsonStr,filePath);
        res="成功";
        long endTime=System.currentTimeMillis();
        System.out.println("Javabean方式程序运行时间： "+(endTime-startTime)+"ms");
        return res;
    }

}
