import java.io.*;
import java.util.*;

public class B_11005 {
    public static void main(String[] args) throws IOException {
    
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));

        String str = br.readLine();

        StringTokenizer st = new StringTokenizer(str);

        int n = Integer.parseInt(st.nextToken());
        int b = Integer.parseInt(st.nextToken());


        String ans = Integer.toString(n, b);
        bw.write(ans.toUpperCase()+"\n");
        bw.flush();
        bw.close();

    }
}
