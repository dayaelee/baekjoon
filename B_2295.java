import java.io.*;
import java.util.*;

public class Main {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        
        String str = br.readLine();
        int n = Integer.parseInt(str);

        int[] arr = new int[n];
        
        
        for(int i = 0; i<n; i++){
            str = br.readLine();
            arr[i]=Integer.parseInt(str);            
        }

        int[] sum = new int[n*(n+1)/2];
        int summIdx=0;
        for(int i = 0; i<n; i++){
            for(int j = i; j<n; j++){
                sum[summIdx++] = arr[i] + arr[j]; 
            }
        }
        int ans=0;
        Arrays.sort(sum);
        for(int i = 0; i<n; i++){
            for(int j = 0; j<n; j++){
                if(Arrays.binarySearch(sum, (arr[i] - arr[j]))>=0){
                    ans = Math.max(ans, (arr[i]));
                } 
            }
        }

        System.out.println(ans);
    }
    
}
