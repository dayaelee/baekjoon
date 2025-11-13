import java.io.*;
import java.util.*;

public class Main {
    
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        String str = br.readLine();
        int n = Integer.parseInt(str);

        int sum = 0;
        for (int i = 0; i<n; i++){
            str = br.readLine();
            int num = Integer.parseInt(str);
            sum+=num;
        }
        
        System.out.println(sum);
        
    }
}
