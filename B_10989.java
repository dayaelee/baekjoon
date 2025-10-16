import java.io.*;
import java.util.*;

public class B_10989 {

    public static void main(String[] args) throws IOException{

        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));

        String str = br.readLine();

        int n = Integer.parseInt(str);

        int[] arr = new int[100001];
        
        while(n-- > 0){
            str = br.readLine();
            arr[Integer.parseInt(str)]+=1;
        }

        for (int i = 1; i<10001; i++ ){
            if (arr[i]>=1){
                while(arr[i]-- > 0){
                    bw.write(i+"\n");
                }
            }
        }

        bw.flush();
        bw.close();

    }
    
}
