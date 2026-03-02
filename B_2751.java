import java.util.*;
import java.io.*;
public class Main {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));
        String str = br.readLine();

        int n = Integer.parseInt(str);

        Integer[] arr = new Integer[n];

        for(int i = 0; i<n; i++){
            str = br.readLine();
            int value = Integer.parseInt(str);
            arr[i]=value;
        }

        Arrays.sort(arr);



        for(int i = 0; i<n; i++){
            bw.write(arr[i] + "\n");
        }

        bw.flush();


        
    }
    
}
