package com.felix.finance.controller;

import com.felix.finance.service.FinanceSrv;
import com.felix.finance.util.FileUtils;
import com.felix.finance.util.PythonUtils;
import org.slf4j.Logger;
import org.slf4j.LoggerFactory;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.web.bind.annotation.CrossOrigin;
import org.springframework.web.bind.annotation.RequestMapping;
import org.springframework.web.bind.annotation.RestController;

import java.io.File;
import java.text.SimpleDateFormat;

@RestController
@RequestMapping("/finance")
@CrossOrigin
public class FinanceController {

    private Logger logger = LoggerFactory.getLogger(this.getClass());

    private static final String separator =File.separator;
    private SimpleDateFormat dateFormat = new SimpleDateFormat("yyyy-MM-dd");

    @Autowired
    private FinanceSrv financeSrv;

//    实时更新数据
    @RequestMapping("/refreshFundData")
    public String refreshFundData(){
        File directory = new File("");//设定为当前文件夹
        String pythonPath=directory.getAbsolutePath()+separator+"script"+separator+"refreshFundData.py";
        logger.info("开始执行实时数据脚本"+pythonPath);
        return PythonUtils.executePython(pythonPath);
    }

    //    生成今日配置文件
    @RequestMapping("/generateNewFundJson")
    public String generateNewFundJson(){
        File directory = new File("");//设定为当前文件夹
        String pythonPath=directory.getAbsolutePath()+separator+"script"+separator+"generateNewFundJson.py";
        logger.info("开始执行生成今日配置脚本"+pythonPath);
        return PythonUtils.executePython(pythonPath);
    }

//    获取今日配置文件内容
    @RequestMapping("/getTodayfundjson")
    public String getTodayfundjson(){
        logger.info("开始获取今日配置");
        File directory = new File("");
        String filePath= directory.getAbsolutePath()+separator+"script"+separator+"fund.json";
        return FileUtils.getfileContent(filePath);
    }

//    更新配置文件
    @RequestMapping("/updatefundjson")
    public String updatefundjson(){
        logger.info("开始更新今日配置");
        String lastTradingDate = getLastTradingDate();
        return financeSrv.updatefundjson(lastTradingDate);
    }


    //    更新单个基金配置文件
    @RequestMapping("/changeJsonByCode")
    public String changeJsonByCode(String fundcode,String fundamount,String add,String amountChange){
        logger.info("fundcode:," + fundcode + "fundamount:," +fundamount+ "add:,"+add+ "amountChange:"+amountChange);
        String res=financeSrv.changeJsonByCode(fundcode,add,amountChange,fundamount);
        return res;
    }

    //    添加一组数据
    @RequestMapping("/addJsonData")
    public String addJsonData(String fundcode,String fundamount){
        logger.info("fundcode:" + fundcode + "fundamount:" +fundamount);
        String res = financeSrv.addJsonData(fundcode,fundamount);
        return res;
    }

    //    获取上一个交易日日期
    @RequestMapping("/getLastTradingDate")
    public String getLastTradingDate(){
            File directory = new File("");//设定为当前文件夹
            String pythonPath= directory.getAbsolutePath()+separator+"script"+separator+"getLastTradingDate.py";
            logger.info("开始执行获取上一个交易日日期脚本："+pythonPath);
            return PythonUtils.executePython(pythonPath);
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
