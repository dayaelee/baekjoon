
import java.io.*;
import java.util.*;

public class Main {
    public static int n, m;
    public static int[] arr;

    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        String str = br.readLine();

        StringTokenizer st = new StringTokenizer(str);
        n = Integer.parseInt(st.nextToken());
        m = Integer.parseInt(st.nextToken());

        arr = new int[n];

        int left=0;
        int right=0;

        for(int i = 0; i<n; i++){
            str = br.readLine();
            arr[i]=Integer.parseInt(str);
            left = Math.max(left, arr[i]);
            right+=arr[i];
        }

        int answer=right;

        while(left <=right){
            int mid = (left+right)/2; 
            if (checking(mid)==1){
                answer = mid;
                right = mid-1;
            }else{
                left = mid+1;
            }
        }
        System.out.println(answer);
    }

    public static int checking(int mid){
        // 체크하는 곳. 
        int cnt = 1;
        int rightV = mid;
        int now = mid;
        for(int i = 0; i<arr.length; i++){
            if(now-arr[i]<0){
                cnt+=1;
                now=rightV;
                if (now-arr[i]<0){
                    return 0;
                }
            }
            now-=arr[i];
        }

        if(cnt<=m) {
            return 1;
        }
        return 0;
    }
}
