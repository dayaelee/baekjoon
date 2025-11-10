import java.io.*;
import java.util.*;

public class Main {
    
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        //BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));
        String str = br.readLine();
        int n = Integer.parseInt(str);
        
        System.out.println(n/10);
        // bw.write(n/10);

        // bw.flush();
        // bw.close();
    }
}
