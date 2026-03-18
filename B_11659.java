import java.util.*;
import java.io.*;


public class Main {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        String str = br.readLine();

        StringTokenizer st = new StringTokenizer(str);

        int n = Integer.parseInt(st.nextToken());
        int m = Integer.parseInt(st.nextToken());

        int[] arr = new int[n+1];
        int[] nu = new int[n+1];
        str = br.readLine();
        st = new StringTokenizer(str);

        for(int i = 1; i<=n; i++){
            arr[i]=Integer.parseInt(st.nextToken());
            if (i ==1){
                nu[i]=arr[i];
            } else{
                nu[i]+=nu[i-1]+arr[i];
            }
        }

        for(int i = 0; i<m; i++){
            str = br.readLine();
            st = new StringTokenizer(str);   
            int a =Integer.parseInt(st.nextToken());
            int b = Integer.parseInt(st.nextToken());

            System.out.println(nu[b]-nu[a-1]);
        }
        
    }
    
}
