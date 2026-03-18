import java.io.*;
import java.util.*;

public class Main {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));
        String str = br.readLine();
        int n = Integer.parseInt(str);
        
        int[] arr = new int[n];
        str = br.readLine();
        StringTokenizer st = new StringTokenizer(str);
        for(int i = 0; i<n; i++){
            arr[i]=Integer.parseInt(st.nextToken());            
        }

        str = br.readLine();
        int m = Integer.parseInt(str);

        int[] check = new int[m];
        str = br.readLine();
        st = new StringTokenizer(str);
        for(int i = 0; i<m; i++){
            check[i]=Integer.parseInt(st.nextToken());            
        }

        Arrays.sort(arr);

        for(int i = 0; i<m; i++){
            int idx = Arrays.binarySearch(arr, check[i]);
            bw.write((idx>=0? 1:0)+"\n");
        }

        bw.flush();
        bw.close();
    }
}
