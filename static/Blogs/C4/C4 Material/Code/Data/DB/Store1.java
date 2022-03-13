/*package web;*/

import java.io.File;
import java.io.FileInputStream;
import java.io.FileReader;
import java.io.BufferedReader;
import java.sql.Connection;
import java.sql.DriverManager;
import java.sql.PreparedStatement;
import java.sql.ResultSet;
import java.sql.SQLException;

public class Store {
    private String dbDriver;
    private String dbURL;
    private String dbUser;
    private String dbPassword;
    private Connection con;
    private PreparedStatement ps;
    public Store() {
        dbDriver = "com.mysql.cj.jdbc.Driver";
        dbURL = "jdbc:mysql://localhost:3306/c4?useSSL=false&allowPublicKeyRetrieval=true&serverTimezone=UTC";
        dbUser = "root";//
        dbPassword = "DB666SHEM";
        initDB();
    }
    public Store(String strDriver, String strURL,
                         String strUser, String strPwd) {
        dbDriver = strDriver;
        dbURL = strURL;
        dbUser = strUser;
        dbPassword = strPwd;
        initDB();
    }
    public void initDB() {
        try {
	Connection conn;
      	ResultSet res;
            // Load Driver
            Class.forName(dbDriver); //.newInstance();
            // Get connection
            con = DriverManager.getConnection(dbURL,
                    dbUser, dbPassword);
        } catch(ClassNotFoundException e) {
            System.out.println(e.getMessage());
        } catch(SQLException ex) {
            // handle any errors
            System.out.println("SQLException: " + ex.getMessage());
            System.out.println("SQLState: " + ex.getSQLState());
            System.out.println("VendorError: " + ex.getErrorCode());
        } catch (Exception e) {
            System.out.println(e.getMessage());
        }
    }
    public boolean storeImg(String strFile) throws Exception {
        boolean written = false;
        if (con == null)
            written = false;
        else {
            int id = 0;
            File filed = new File(strFile);
            if (filed.isDirectory()) {
                String s[] = filed.list();
                for (int i = 0; i < s.length; i++) {
                    File file = new File(strFile + "/" + s[i]);

                    if (file.isDirectory()) {
                        System.out.println(s[i] + " is a directory");
                    } else if(!s[i].equals(".DS_Store")){
                        FileInputStream fis = new FileInputStream(file);
                        try {
                            ps = con.prepareStatement("SELECT MAX(id) FROM PIC");
                            ResultSet rs = ps.executeQuery();
                            if(rs != null) {
                                while(rs.next()) {
                                    if(id==0)
                                        id = rs.getInt(1)+1;
                                    else
                                        id=rs.getInt(1);
                                }
                            } else {
                                return written;
                            }
                            ps = con.prepareStatement("insert "
                                    + "into PIC values (?,?,?)");
                            ps.setInt(1, id);
                            ps.setString(2, file.getName());
                            ps.setBinaryStream(3, fis, (int) file.length());
                            ps.executeUpdate();
                            written = true;
                        } catch (SQLException e) {
                            written = false;
                            System.out.println("SQLException: "
                                    + e.getMessage());
                            System.out.println("SQLState: "
                                    + e.getSQLState());
                            System.out.println("VendorError: "
                                    + e.getErrorCode());
                            e.printStackTrace();
                        } finally {
                            
                        }
                    }
                }
            }
        }
        return written;
    }
    public boolean storetxt(String strFile,String txtname) throws Exception{
        boolean flag=false;
        File file = new File(strFile);
        BufferedReader read =null;
        try{
            read = new BufferedReader(new FileReader(file));
            int num=0;
            String c;
            int id=0;
            while((c=read.readLine())!=null){                     
            	int length=c.length();
                	for(int t=0;t<length;t++) {
                		num=num*10+(c.charAt(t)-'0');
                	}                              
                    ps = con.prepareStatement("SELECT MAX(id) FROM "+txtname);
                    ResultSet rs = ps.executeQuery();
                    if(rs != null) {
                    	while(rs.next()) {
                            if(id==0)
                                id = rs.getInt(1)+1;
                            else
                                id=rs.getInt(1);
                        }     
                    } else {
                        return flag;
                    }
                    ps = con.prepareStatement("insert into "+txtname+" values (?,?)");
                    ps.setInt(1, id);
                    ps.setInt(2, num);
                    ps.executeUpdate();
                    flag = true;
                    num=0;
                
            }
        }catch (SQLException e){

        }
        read.close();
        return flag;
    }
    
    public static void main(String[] args) {
        boolean flag = false;
        Store sp = new Store();
      
        
        try {
            flag = sp.storetxt("D:/Document/Creat/magic/Python/C4/Data/Sensor_data/data1/Pulse.txt",
                    "pulse");
        } catch (Exception e) {
            e.printStackTrace();
        }
        if(flag) {
            System.out.println("pulse uploading is successful.");
        } else {
            System.out.println("pulse uploading is failed.");
        }
        
        
        try {
            flag = sp.storetxt("D:/Document/Creat/magic/Python/C4/Data/Sensor_data/data1/Sound.txt",
                    "sound");
        } catch (Exception e) {
            e.printStackTrace();
        }
        if(flag) {
            System.out.println("sound uploading is successful.");
        } else {
            System.out.println("sound uploading is failed.");
        }

        try {
            flag = sp.storetxt("D:/Document/Creat/magic/Python/C4/Data/Sensor_data/data1/Attention.txt",
                    "Attention");
        } catch (Exception e) {
            e.printStackTrace();
        }
        if(flag) {
            System.out.println("Attention uploading is successful.");
        } else {
            System.out.println("Attention uploading is failed.");
        }
        
        try {
            flag = sp.storetxt("D:/Document/Creat/magic/Python/C4/Data/Sensor_data/Blink.txt",
                    "Blink");
        } catch (Exception e) {
            e.printStackTrace();
        }
        if(flag) {
            System.out.println("Blink uploading is successful.");
        } else {
            System.out.println("Blink uploading is failed.");
        }
    }
}
