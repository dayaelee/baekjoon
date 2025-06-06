public class 15787 {
    
}
import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.Arrays;
import java.util.HashSet;
import java.util.StringTokenizer;

public class Main {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        String str = br.readLine();
        StringTokenizer st = new StringTokenizer(str);
        
        int n = Integer.parseInt(st.nextToken());
        int m = Integer.parseInt(st.nextToken());

        int[][] arr = new int[n][20];

        for (int i = 0; i < n; i++) {
            for (int j = 0; j < 20; j++) {
                arr[i][j]=0;
            }
        }

        for (int i = 0; i < m; i++) {
            String str2 = br.readLine();
            StringTokenizer st2 = new StringTokenizer(str2);

            int o = Integer.parseInt(st2.nextToken());
            int ii = Integer.parseInt(st2.nextToken());

            if (o==1 || o==2){
                int t = Integer.parseInt(st2.nextToken());

                if (o==1){
                    if (arr[ii-1][t-1]==0){
                        arr[ii-1][t-1]=1;
                    }
                } else if (o==2){
                    if (arr[ii-1][t-1]==1){
                        arr[ii-1][t-1]=0;
                    }
                }
            }

            if (o==3){
                for (int j = 19; j > 0; j--) {
                    arr[ii-1][j] = arr[ii-1][j-1];
                }
                arr[ii-1][0]=0;
            } else if (o==4){
                for (int j = 1; j < 20; j++) {
                    arr[ii-1][j-1] = arr[ii-1][j];
                }
                arr[ii-1][19]=0;
            }
        }

        HashSet<String> set = new HashSet<>(n);
        StringBuilder sb = new StringBuilder(20);

        for (int i = 0; i < n; i++) {
            sb.setLength(0);
            for (int j = 0; j < 20; j++) {
                sb.append(arr[i][j]);
            }
            set.add(sb.toString());
        }

        System.out.println(set.size());
    }
}