import java.io.*;
import java.util.*;
public class Main {
    public static void main(String[] args) throws IOException   {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        String str = br.readLine();

        StringTokenizer st = new StringTokenizer(str);
        int n = Integer.parseInt(st.nextToken());
        Long m = Long.parseLong(st.nextToken());

        int[] arr = new int[n];
        str = br.readLine();
        st = new StringTokenizer(str);
        
        long ans = 0; 
        long maxX =0;
        long minX =0;
        for(int i = 0; i<n; i++){
            arr[i] = Integer.parseInt(st.nextToken());
            maxX=Math.max(arr[i], maxX);
        }

        long l = minX, r=maxX;
        while(l<=r){
            long tmp = 0; 
            long minV = (l+r)/2;

            for(int i = 0; i<n; i++){
                if(arr[i]-minV>=0)
                    tmp += arr[i]-minV;
            }

            if(tmp>=m){
                if (ans<=minV){
                    ans = minV;
                    l=minV+1;
                }
                
            }else{
                r=minV-1;
            }
        }
        System.out.println(ans);
    }
}
