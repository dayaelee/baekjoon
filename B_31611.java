import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.sql.SQLOutput;
import java.util.*;

public class B_31611 {
    public static boolean flag;
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        String str = br.readLine();
        int x = Integer.parseInt(str);

        // 2일후 화요일
        // 9일후 화요일
        // 16일후 화요일

        int t = 9;

        flag = false;
        if (x==2){
            flag = true;
            System.out.println(1);
        } else if (x>=2) {
            while (t<=100){
                if (x==t){
                    flag = true;
                    System.out.println(1);
                    break;
                }else {
                    t+=7;
//                    System.out.println(t);
                }
            }
            if (!flag){
                System.out.println(0);
            }
        } else  {
            System.out.println(0);
        }
    }
}

