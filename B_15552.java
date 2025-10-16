import java.io.*;
import java.util.*;

public class B_15552 {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));
        String str = br.readLine();

        int t = Integer.parseInt(str);
        while (t-- >0){
            str = br.readLine();
            StringTokenizer st = new StringTokenizer(str);
            int a = Integer.parseInt(st.nextToken());
            int b = Integer.parseInt(st.nextToken());

            bw.write(a+b +"\n");
            
            
        }

        bw.flush();
        bw.close();

    }
    
}
