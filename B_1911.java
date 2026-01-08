import java.io.*;
import java.util.*;

public class Main {
    public static int N, L;
    public static int[][] arr;

    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        String str = br.readLine();

        StringTokenizer st = new StringTokenizer(str);
        N = Integer.parseInt(st.nextToken());
        L = Integer.parseInt(st.nextToken());

        arr = new int[N][2];
        for(int i = 0; i<N; i++){
            str = br.readLine();
            st = new StringTokenizer(str);

            int a = Integer.parseInt(st.nextToken());
            int b = Integer.parseInt(st.nextToken());
            arr[i][0]=a;
            arr[i][1]=b;
        }

        Arrays.sort(arr, (o1, o2)-> o1[0]-o2[0]);

        long ans = 0;
        long pos = 0;

        for (int i = 0; i < N; i++) {
            long a = arr[i][0];
            long b = arr[i][1];

            long start = Math.max(a, pos);
            if (start >= b) continue;

            long len = b - start;
            long cnt = len / L;
            if (len % L != 0) cnt++;
            // long cnt = (len + L - 1) / L;

            ans += cnt;
            pos = start + cnt * L;
        }


        System.out.println(ans);
    }
    
}
