import java.io.*;
import java.util.*;

public class Main {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));
        String str = br.readLine();
        StringTokenizer st = new StringTokenizer(str);

        int n = Integer.parseInt(st.nextToken());
        int m = Integer.parseInt(st.nextToken());

        int[] arr = new int[n+2];
        str = br.readLine();
        st = new StringTokenizer(str);
        for(int i = 1; i<=n; i++){
            arr[i]=Integer.parseInt(st.nextToken());
        }

        int check[] = new int[n+2];
        for(int i = 0; i<m; i++){
            str = br.readLine();
            st = new StringTokenizer(str);
            int s = Integer.parseInt(st.nextToken());
            int e = Integer.parseInt(st.nextToken());
            int v = Integer.parseInt(st.nextToken());

            check[s]+=v;
            check[e+1]+=(-v);
        }

        int acc[] = new int[n+2];
        for(int i = 1; i<=n; i++){
            acc[i]=acc[i-1]+check[i];
        }
        
        for(int i = 1; i<=n; i++){
            arr[i]+=acc[i];
            bw.write(arr[i]+" ");
        }

        bw.newLine();
        bw.flush();
        bw.close();
    }
}
