package com.felix.finance.util;

import org.slf4j.Logger;
import org.slf4j.LoggerFactory;

import java.io.BufferedReader;
import java.io.InputStreamReader;

public class PythonUtils {

    private static Logger logger = LoggerFactory.getLogger("com.felix.finance.util.PythonUtils");

    public static String executePython(String pythonPath){
        try {
            String[] args1 = new String[] { "python", pythonPath};
            Process pr=Runtime.getRuntime().exec(args1);
            BufferedReader in = new BufferedReader(new InputStreamReader(
                    pr.getInputStream(), "GBK"));
            String line;
            StringBuilder sb=new StringBuilder();
            while ((line = in.readLine()) != null) {
                sb.append(line);
            }
            in.close();
            pr.waitFor();
            return sb.toString();
        }
        catch (Exception e) {
            logger.info(e.getMessage());
            e.printStackTrace();
            return e.getMessage();
        }
    }
}
