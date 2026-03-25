import java.io.*;
import java.util.*;

public class Main {
    public static void main(String[] args) throws IOException {
        BufferedReader  br = new BufferedReader(new InputStreamReader(System.in));

        String str = br.readLine();
        StringTokenizer st = new StringTokenizer(str);

        int n, m; 
        n = Integer.parseInt(st.nextToken());
        m = Integer.parseInt(st.nextToken());

        long[] arr = new long[m];
        
        long r = 0;
        for(int i = 0; i<m; i++){
            arr[i]=Long.parseLong(br.readLine());
            r = Math.max(r, arr[i]);
        }

        long l = 1;
        long ans = -1;
        
        
        while(l<=r){
            long now = (l+r)/2; // 길이 

            int cnt = 0; // 값
            for(int i = 0; i<m; i++){
                if(arr[i]%now==0){ 
                    cnt+=arr[i]/now;
                }else{
                    cnt+=((arr[i]/now)+1);
                }
            }
            
            if(cnt<=n){
                ans = now;
                r=now-1;
            }else{
                l=now+1;
            }
        }

        
        System.out.println(ans);

    }
    
}
