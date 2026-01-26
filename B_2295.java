import java.util.*;
import java.io.*;

public class Main {
    public static int n;
    public static long[] arr;
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        String str = br.readLine();

        n = Integer.parseInt(str);

        arr = new long[n];
        for(int i = 0; i<n; i++){
            str = br.readLine();
            arr[i] = Long.parseLong(str);
        }

        Arrays.sort(arr);

        long[] ts = new long[n * (n + 1) / 2];
        int idx = 0; 
        for(int i = 0; i<n; i++){
            for(int j = i; j<n; j++){
                ts[idx++] = arr[i] + arr[j];
            }
        }

        Arrays.sort(ts);
        
        for(int i = n-1; i>=0; i--){
            for(int j = 0; j<n; j++){
                long target = arr[i]-arr[j];
                if (Arrays.binarySearch(ts, target)>=0){
                    System.out.println(arr[i]);
                    return; 
                }
            }
        }
        
    }
    
}
