import java.util.*;
import java.io.*;

public class Main {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        
        String s = br.readLine();
        StringTokenizer st = new StringTokenizer(s);

        int n = Integer.parseInt(st.nextToken());
        int k = Integer.parseInt(st.nextToken());
        int b = Integer.parseInt(st.nextToken());

        boolean[] lightsOff = new boolean[n+1];

        int[] lOffnu = new int[n+1];
        
        for(int i = 0; i<b; i++){
            s = br.readLine();
            int t = Integer.parseInt(s);
            lightsOff[t]=true;
            
        }

        // 고장 누적합 
        for(int i = 1; i<n+1; i++){
            if(lightsOff[i]==true)
                lOffnu[i]=lOffnu[i-1]+1;
            else{
                lOffnu[i]=lOffnu[i-1];
            }
        }

        // 슬라이딩 윈도우
        int ans=n;

        int start=0, end=start+k;
        while(true){
            if(lOffnu[end]-lOffnu[start]>=0)
                ans = Math.min(lOffnu[end]-lOffnu[start], ans);
            if (end>=n){
                break;
            }
            start+=1;
            end+=1;
        }

        System.out.println(ans);
    }
    
}
