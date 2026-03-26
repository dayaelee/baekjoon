import java.io.*;
import java.util.*;
public class Main {
    public static void main(String[] args) throws IOException {


        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));

        String str = br.readLine();

        StringTokenizer st = new StringTokenizer(str);
        int n = Integer.parseInt(st.nextToken());
        int m = Integer.parseInt(st.nextToken());

        int[] arr = new int[n];


        str = br.readLine();
        st = new StringTokenizer(str);
        for(int i = 0; i<n; i++){
            arr[i]=Integer.parseInt(st.nextToken());
        }

        int l = 0, r = 0;
        
        int sum = 0;
        int cnt = 0;
        while(true){
            if(sum>=m){
                sum-=arr[l];
                l+=1;
            } else if (r>=n) {
                break;
            } 
            else{
                sum+=arr[r];
                r+=1; 
            }
            
            if(sum == m){
                cnt++;
            }

        }

        System.out.println(cnt);


    }
    
}
