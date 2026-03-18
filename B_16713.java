import java.util.*;
import java.io.*;

public class Main {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        String str = br.readLine();

        StringTokenizer st = new StringTokenizer(str);
        int n = Integer.parseInt(st.nextToken());
        int q = Integer.parseInt(st.nextToken());

        str = br.readLine();
        int[] intArr = new int[n+1];

        st = new StringTokenizer(str);
        for(int i = 0; i<=n; i++){
            if (i==0){
                intArr[i]=0;
            }else{
                intArr[i]=Integer.parseInt(st.nextToken());
            }
        }

        int[] nu = new int[n+1];

        for(int i = 1; i<=n; i++){
            if (i ==1){
                nu[i] = intArr[i];
            }else{
                nu[i]= nu[i-1] ^ intArr[i];
            }
        }

        int sum=0;
        for(int i = 0; i<q; i++){
            str = br.readLine();
            st = new StringTokenizer(str);
            int a = Integer.parseInt(st.nextToken());
            int b = Integer.parseInt(st.nextToken());
            sum ^= nu[b] ^ nu[a-1];
        }
        System.out.println(sum);
    }
    
}
