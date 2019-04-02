package com.felix.finance.controller;

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

@RestController
@RequestMapping("/finance")
@CrossOrigin
public class IndexController {

    private Logger logger = LoggerFactory.getLogger(this.getClass());

    private static final String separator =File.separator;
    private SimpleDateFormat dateFormat = new SimpleDateFormat("yyyy-MM-dd");

    @Autowired
    private FinanceSrv financeSrv;

//    获取今日配置文件内容
    @RequestMapping("/getIndexInfo")
    public String getIndexInfo(){
        logger.info("开始获取指数信息");
        File directory = new File("");
        String filePath= directory.getAbsolutePath()+separator+"script"+separator+"getindexData.py";
        return PythonUtils.executePython(filePath);
    }


    @RequestMapping(value = "/getImg",produces = MediaType.IMAGE_JPEG_VALUE)
    public byte[] getImage(String imgName) throws IOException {
        File directory = new File("");
        String filePath= directory.getAbsolutePath()+separator+"data"+separator+"indexImg"+separator+imgName+".png";
        File file = new File(filePath);
        FileInputStream inputStream = new FileInputStream(file);
        byte[] bytes = new byte[inputStream.available()];
        inputStream.read(bytes, 0, inputStream.available());
        return bytes;
    }


    public static void main(String[] args){
        File directory = new File("");//设定为当前文件夹
        try{
            System.out.println(directory.getCanonicalPath());//获取标准的路径
            System.out.println(directory.getAbsolutePath());//获取绝对路径
        }catch(Exception e){}
    }
}
