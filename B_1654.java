import java.io.*;
import java.util.*;

public class Main {
    public static void main(String[] args) throws IOException {
        BufferedReader  br = new BufferedReader(new InputStreamReader(System.in));
        String str = br.readLine();
        StringTokenizer st = new StringTokenizer(str);

        int k;
        int n;
        k = Integer.parseInt(st.nextToken());
        n = Integer.parseInt(st.nextToken());

        long[] arr = new long[n];

        
        long r = 0L;
        long l = 1L;
        for(int i =0; i<k; i++){
            str = br.readLine();
            arr[i] = Long.parseLong(str);

            r = Math.max(arr[i], r);
        }

        long answer = 0;

        while(l<=r){
            long m = (l+r)/2;

            if (m==0){
                break;
            }

            long v = 0;
            
            for(int i = 0; i<n; i++){
                v+=arr[i]/m;
            }
            if(v>=n){
                answer=Math.max(answer, m);
                l=m+1;
            }else{
                r=m-1;
            }

            
        }

        System.out.println(answer);
        
    }
    
}
