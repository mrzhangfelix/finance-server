package com.felix.finance.controller;

import com.alibaba.fastjson.JSON;
import com.alibaba.fastjson.JSONArray;
import com.alibaba.fastjson.JSONObject;
import com.felix.finance.util.FileUtils;
import org.slf4j.Logger;
import org.slf4j.LoggerFactory;
import org.springframework.web.bind.annotation.CrossOrigin;
import org.springframework.web.bind.annotation.RequestMapping;
import org.springframework.web.bind.annotation.RestController;

import java.io.BufferedReader;
import java.io.File;
import java.io.IOException;
import java.io.InputStreamReader;
import java.text.SimpleDateFormat;
import java.util.Calendar;
import java.util.Date;

@RestController
@RequestMapping("/finance")
@CrossOrigin
public class FinanceController {

    private Logger logger = LoggerFactory.getLogger(this.getClass());

    private static final String separator =File.separator;


    @RequestMapping("/fundIncome")
    public String getbyicare(String num){
        try {
            File directory = new File("");//设定为当前文件夹
            String[] args1 = new String[] { "python", directory.getAbsolutePath()+separator+"script"+separator+"fundIncome.py"};
            logger.info(directory.getAbsolutePath()+separator+"script"+separator+"fundIncome.py");
            Process pr=Runtime.getRuntime().exec(args1);
            BufferedReader in = new BufferedReader(new InputStreamReader(
                    pr.getInputStream(), "GBK"));
            String line;
            StringBuilder sb=new StringBuilder();
            while ((line = in.readLine()) != null) {
                sb.append(line);
            }
            logger.info("res::"+sb.toString());
            in.close();
            pr.waitFor();
            return sb.toString();
        }
        catch (Exception e) {
            logger.info(e.getMessage());
            e.printStackTrace();
        }
        return "group_name_list_error";
    }

//    实时更新数据
    @RequestMapping("/refreshFundData")
    public String refreshFundData(){
        try {
            File directory = new File("");//设定为当前文件夹
            String[] args1 = new String[] { "python", directory.getAbsolutePath()+separator+"script"+separator+"refreshFundData.py"};
            logger.info(directory.getAbsolutePath()+separator+"script"+separator+"refreshFundData.py");
            Process pr=Runtime.getRuntime().exec(args1);
            BufferedReader in = new BufferedReader(new InputStreamReader(
                    pr.getInputStream(), "GBK"));
            String line;
            StringBuilder sb=new StringBuilder();
            while ((line = in.readLine()) != null) {
                sb.append(line);
            }
            logger.info("res::"+sb.toString());
            in.close();
            pr.waitFor();
            return sb.toString();
        }
        catch (Exception e) {
            logger.info(e.getMessage());
            e.printStackTrace();
        }
        return "updetefundjson_error";
    }

//    获取今日配置文件内容
    @RequestMapping("/getTodayfundjson")
    public String getTodayfundjson(){
        logger.info("开始获取今日配置");
        File directory = new File("");
        String filePath= directory.getAbsolutePath()+separator+"script"+separator+"fund.json";
        StringBuffer sb = new StringBuffer();
        try {
            FileUtils.readToBuffer(sb, filePath);
        } catch (IOException e) {
            e.printStackTrace();
        }
        logger.info("今日配置：："+sb.toString());
        return sb.toString();
    }

//    更新配置文件
    @RequestMapping("/updatefundjson")
    public String updatefundjson(){
        logger.info("开始更新今日配置");
        String res="失败";
        File directory = new File("");
        Date now = new Date();
        SimpleDateFormat dateFormat = new SimpleDateFormat("yyyy-MM-dd");//可以方便地修改日期格式
        Calendar calendar = Calendar.getInstance();
        calendar.setTime(now);
        calendar.set(Calendar.DATE, calendar.get(Calendar.DATE) - 1);
        String yesterday = dateFormat.format( calendar.getTime() );
        String newfilePath= directory.getAbsolutePath()+separator+"history"+separator+yesterday+".json";
        String filePath= directory.getAbsolutePath()+separator+"script"+separator+"fund.json";
        File source=new File(newfilePath);
        File dest=new File(filePath);
        try {
            FileUtils.copyFileUsingFileStreams(source,dest);
        } catch (IOException e) {
            e.printStackTrace();
        }
        res="成功";
        logger.info("更新配置：："+res);
        return res;
    }


    //    更新单个基金配置文件
    @RequestMapping("/changeJsonByCode")
    public String changeJsonByCode(String fundcode,
                                   String fundamount,
                                   String add,
                                   String amountChange){
        logger.info("fundcode:," + fundcode + "fundamount:," +fundamount+ "add:,"+add+ "amountChange:"+amountChange);
        String res="失败";
        File directory = new File("");
        String filePath= directory.getAbsolutePath()+separator+"script"+separator+"fund.json";
        StringBuffer sb = new StringBuffer();
        try {
            FileUtils.readToBuffer(sb, filePath);
        } catch (IOException e) {
            e.printStackTrace();
        }
        logger.info("今日配置：："+sb.toString());
        JSONObject obj = JSON.parseObject(sb.toString());
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
        logger.info("更新配置：："+res);
        return res;
    }


    //    添加一组数据
    @RequestMapping("/addJsonData")
    public String addJsonData(String fundcode,
                                   String fundamount){
        logger.info("fundcode:," + fundcode + "fundamount:," +fundamount);
        String res="失败";
        File directory = new File("");
        String filePath= directory.getAbsolutePath()+separator+"script"+separator+"fund.json";
        StringBuffer sb = new StringBuffer();
        try {
            FileUtils.readToBuffer(sb, filePath);
        } catch (IOException e) {
            e.printStackTrace();
        }
        JSONObject obj = JSON.parseObject(sb.toString());
        JSONArray fundlist=(JSONArray)obj.get("fundlist");
        JSONObject newfund=new JSONObject();
        newfund.put("fundamount",fundamount);
        newfund.put("fundcode",fundcode);
        fundlist.add(newfund);
//        String filePathtest= directory.getAbsolutePath()+separator+"script"+separator+"fundtest.json";
        FileUtils.writeStringtoFile(obj.toString(),filePath);
        res="成功";
        logger.info("添加数据：："+res);
        return res;
    }

    @RequestMapping("/test")
    public String test(String num){
        return "success";
    }

    public static void main(String[] args){
        File directory = new File("");//设定为当前文件夹
        try{
            System.out.println(directory.getCanonicalPath());//获取标准的路径
            System.out.println(directory.getAbsolutePath());//获取绝对路径
        }catch(Exception e){}
    }
}
