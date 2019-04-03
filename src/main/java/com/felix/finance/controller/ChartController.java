package com.felix.finance.controller;

import com.felix.finance.entity.Profit;
import com.felix.finance.service.FinanceSrv;
import com.felix.finance.util.FileUtils;
import com.felix.finance.util.PythonUtils;
import org.slf4j.Logger;
import org.slf4j.LoggerFactory;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.http.MediaType;
import org.springframework.web.bind.annotation.CrossOrigin;
import org.springframework.web.bind.annotation.RequestMapping;
import org.springframework.web.bind.annotation.RestController;

import java.io.File;
import java.io.FileInputStream;
import java.io.IOException;
import java.text.SimpleDateFormat;
import java.util.ArrayList;
import java.util.Date;
import java.util.HashMap;
import java.util.List;

@RestController
@RequestMapping("/finance")
@CrossOrigin
public class ChartController {

    private Logger logger = LoggerFactory.getLogger(this.getClass());

    private static final String separator =File.separator;
    private SimpleDateFormat dateFormat = new SimpleDateFormat("yyyy-MM-dd");

    @Autowired
    private FinanceSrv financeSrv;

//    获取今日配置文件内容
    @RequestMapping("/getYingliList")
    public List getYingliList(){
        logger.info("开始获取今日盈利分时数据");
        String res="";
        File directory = new File("");
        String today=dateFormat.format(new Date());
        String filePath= directory.getAbsolutePath()+separator+"data"+separator+"yingliList"+separator+today+".txt";
        String str = FileUtils.getfileContent(filePath);
        String[] strList=str.split(";\n");
        List resList=new ArrayList();
        for(String i : strList){
            if (i.equals("\n")){
                continue;
            }
            String[] iStr=i.split(",");
            String time=iStr[0];
            String yingli=iStr[1];
//            HashMap<String,String> map=new HashMap<String, String>();
//            map.put("时间", time);
//            map.put("盈利", yingli);
            Profit profit=new Profit(yingli,time);
            resList.add(profit);
        }
        return resList;
    }


    public static void main(String[] args){
        File directory = new File("");//设定为当前文件夹
        try{
            System.out.println(directory.getCanonicalPath());//获取标准的路径
            System.out.println(directory.getAbsolutePath());//获取绝对路径
        }catch(Exception e){}
    }
}
