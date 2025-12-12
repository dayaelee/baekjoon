import java.io.*;
import java.util.*;

public class Main {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));

        String str = br.readLine();
        String answer = "~~~";

        int n = str.length();
        int a = 1;
        int b = a;

        String tmp = str;
        while(a<=n-3){
            if (b<=n-2){
                b += 1;
            }else{
                a+=1;
                b = a+1;
            }
            String m1 = str.substring(0, a);
            String m2 = str.substring(a, b);
            String m3 = str.substring(b, n);

            StringBuffer sb1 = new StringBuffer(m1);
            String r1 = sb1.reverse().toString();

            StringBuffer sb2 = new StringBuffer(m2);
            String r2 = sb2.reverse().toString();

            StringBuffer sb3 = new StringBuffer(m3);
            String r3 = sb3.reverse().toString();

            // System.out.println(r1 + " " + m1);
            // System.out.println(r2 + " " + m2);
            // System.out.println(r3 + " " + m3);

            String result = r1 + r2 + r3;
            int check = answer.compareTo(result);
            if (check>=0){
                answer = result;
            }
        }
        System.out.println(answer);
    }
}
