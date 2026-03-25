import java.io.*;
import java.util.*;

public class Main {
    public static void main(String[] args) throws IOException {
        BufferedReader  br = new BufferedReader(new InputStreamReader(System.in));



        String str = br.readLine();
        StringTokenizer st = new StringTokenizer(str);

        int n,  m; 
        n = Integer.parseInt(st.nextToken());
        m = Integer.parseInt(st.nextToken());

        int[] arr = new int[n];
        long l=0;
        for(int i = 0; i<n; i++){
            arr[i]=Integer.parseInt(br.readLine());
            l=Math.max(arr[i], l);
        }

        long r = 1000000000;
        long ans = Integer.MAX_VALUE;
        
        while(l<=r){
            long mid = (l+r)/2;
            int cnt = 1;
            long money = mid;

            for(int i = 0; i<n; i++){
                if(money<arr[i]){ // 쓸돈 부족한 경우 
                    cnt+=1;
                    money=mid;
                }
                money-=arr[i];
            }

            
            if(cnt<=m){
                r=mid-1;
                ans = mid;
                // System.out.println("ans: "+ ans);
            }else{
                l=mid+1;
            }
        }

        
        System.out.println(ans);

    }
    
}
