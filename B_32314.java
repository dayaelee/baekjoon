import java.io.*;
import java.util.*;

public class Main {
    public static void main(String[] args) throws IOException {
        BufferedReader  br = new BufferedReader(new InputStreamReader(System.in));

        String str = br.readLine();
        int a = Integer.parseInt(str); // 암페어 


        str = br.readLine();
        StringTokenizer st = new StringTokenizer(str);

        int k; // 와트
        int n; // 볼트
        k = Integer.parseInt(st.nextToken());
        n = Integer.parseInt(st.nextToken());

        if(k/n>=a){
            System.out.println(1);
        }else{
            System.out.println(0);
        }


    }
    
}
