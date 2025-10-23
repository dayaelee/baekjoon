import java.io.*;
import java.util.*;

public class Main{

    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));

        String str = br.readLine();

        int t = Integer.parseInt(str);

        while(t-- > 0){
            str = br.readLine();
            StringTokenizer st = new StringTokenizer(str);
            int h = Integer.parseInt(st.nextToken()); // 층 수
            int w = Integer.parseInt(st.nextToken()); // 호 수 
            int n = Integer.parseInt(st.nextToken()); // N번째로 도착한 손님의 호수? 

            int g = n/h; // 열 
            int last = n%h;
            // String ans = "";
            int tmp;
            int anstmp=-1;
            if (last>0){
                tmp = last;
                // if ((""+g).length()<2){
                //     if(g+1<10){
                //         tmp = tmp+"0";
                //     }
                // }
                anstmp = (g+1);
                // ans = ""+tmp+anstmp;
            }else{
                tmp = h;
                // if ((""+g).length()<2){
                //     tmp = tmp+"0";
                // }
                anstmp = g;
                // ans = ""+tmp+anstmp;
            }
            // bw.write(ans+"\n");
            bw.write(String.format("%d%02d\n", tmp, anstmp));
        }

        bw.flush();
        bw.close();
    }
}
