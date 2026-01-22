import java.util.*;
import java.io.*;

public class Main {

    public static int n, m;
    public static int[] plus;
    public static int[] now;
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        String str = br.readLine();

        StringTokenizer st = new StringTokenizer(str);
        n = Integer.parseInt(st.nextToken());
        m = Integer.parseInt(st.nextToken());

        now = new int[n+2];
        plus = new int[n+2];

        str = br.readLine();
        st = new StringTokenizer(str);
        for(int i = 1; i<=n; i++){
            now[i]=Integer.parseInt(st.nextToken());
        }

        for(int i = 0; i<m; i++){
            str = br.readLine();
            st = new StringTokenizer(str);
            int a = Integer.parseInt(st.nextToken());
            int b = Integer.parseInt(st.nextToken());
            int k = Integer.parseInt(st.nextToken());

            plus[a]+=k;
            plus[b+1]-=k;
        }

        StringBuilder sb = new StringBuilder();
        int acc = 0;
        for(int i = 1; i<=n; i++){
            acc+=plus[i];
            now[i]+=acc;
            sb.append(now[i]+" ");
        }

        System.out.println(sb.toString());


    }
    
}
