package com.felix.finance.util;
import java.io.*;

public class FileUtils {

    private static final String separator =File.separator;
//    读取文件内容到StringBuffer
    public static void readToBuffer(StringBuffer buffer, String filePath) throws IOException {
        InputStream is = new FileInputStream(filePath);
        String line; // 用来保存每行读取的内容
        BufferedReader reader = new BufferedReader(new InputStreamReader(is));
        line = reader.readLine(); // 读取第一行
        while (line != null) { // 如果 line 为空说明读完了
            buffer.append(line); // 将读到的内容添加到 buffer 中
            buffer.append("\n"); // 添加换行符
            line = reader.readLine(); // 读取下一行
        }
        reader.close();
        is.close();
    }

//    拷贝文件
    public static void copyFileUsingFileStreams(File source, File dest)
            throws IOException {
        InputStream input = null;
        OutputStream output = null;
        try {
            input = new FileInputStream(source);
            output = new FileOutputStream(dest);
            byte[] buf = new byte[1024];
            int bytesRead;
            while ((bytesRead = input.read(buf)) > 0) {
                output.write(buf, 0, bytesRead);
            }
        } finally {
            input.close();
            output.close();
        }
    }

//    str写入文件
    public static void writeStringtoFile(String str,String filename){
        FileWriter writer;
        try {
            writer = new FileWriter(filename);
            writer.write(str);
            writer.flush();
            writer.close();
        } catch (IOException e) {
            e.printStackTrace();
        }
    }

//返回文件内容
    public static String getfileContent(String filePath){
        StringBuffer sb = new StringBuffer();
        try {
            FileUtils.readToBuffer(sb, filePath);
        } catch (IOException e) {
            e.printStackTrace();
        }
        return sb.toString();

    }

    public static String getfilePath(String dir,String filename){
        File directory = new File("");
        String filePath= directory.getAbsolutePath()+separator+dir+separator+filename;
        return filePath;
    }
}
