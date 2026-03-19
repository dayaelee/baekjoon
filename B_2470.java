import java.util.*;
import java.io.*; 
public class Main {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        String str = br.readLine();
        int n = Integer.parseInt(str);
        Long[] arr = new Long[n];

        str = br.readLine();
        StringTokenizer st = new StringTokenizer(str);
        for(int i = 0; i<n; i++){
            arr[i]=Long.parseLong(st.nextToken());
        }

        Arrays.sort(arr);

        int l = 0; 
        int r = n-1;

        Long value = Long.MAX_VALUE;

        Long[] rem = new Long[2];


        while(l<r){
            
            if(Math.abs(arr[l]+arr[r])<value){
                value = Math.abs(arr[l]+arr[r]);
                rem[0]=arr[l];
                rem[1]=arr[r];
            }

            if ((arr[l]+arr[r])<0){
                l+=1;
            }else if ((arr[l]+arr[r])>=0){
                r-=1;
            }
        }

        Arrays.sort(rem);
        System.out.println(rem[0]+" "+rem[1]);
    }
    
}
