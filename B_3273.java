import java.util.*;
import java.io.*;
import java.util.stream.*;

public class B_3273 {
    public static void main(String[] args) throws IOException {
        
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        String str = br.readLine();

        int n = Integer.parseInt(str);

        int[] arr = new int[n];
        str = br.readLine();
        StringTokenizer st = new StringTokenizer(str);
        for(int i = 0; i<n; i++){
            arr[i] = Integer.parseInt(st.nextToken());
        }

        str = br.readLine();
        int x = Integer.parseInt(str);

        Arrays.sort(arr); // 오름차순

        int left = 0, right = n-1;
        int ans=0;
        while (left<right){
            int sum = arr[left]+arr[right]; 
            if(sum == x){
                ans+=1;
                left+=1;
                right-=1;
            }else if(sum>x){
                right-=1;
            }else{
                left+=1;
            }
        }

        System.out.println(ans);

    }
}

