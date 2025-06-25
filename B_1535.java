import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.Arrays;
import java.util.StringTokenizer;

public class Main {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));

        int blood = 100;
        int n = Integer.parseInt(br.readLine());
        if (n == 0) {
            System.out.println(0);
        } else {
            String str = br.readLine();
            StringTokenizer st = new StringTokenizer(str);
            int[] nBlood = new int[n];
            int[] nHappy = new int[n];
            for (int i = 0; i < n; i++) {
                nBlood[i] = Integer.parseInt(st.nextToken());
            }
            String str2 = br.readLine();
            st = new StringTokenizer(str2);
            for (int i = 0; i < n; i++) {
                nHappy[i] = Integer.parseInt(st.nextToken());
            }

            int answer = 0;
            int[][] dp = new int[n+1][101];
            for (int i = 1; i < n + 1; i++) {
                for (int j = 1; j < 101; j++) {
                    if (j>=nBlood[i-1]){
                        dp[i][j] = Math.max(dp[i-1][j], dp[i-1][j-nBlood[i-1]]+nHappy[i-1]);
                    }else{
                        dp[i][j]= dp[i-1][j];
                    }
                }
            }
            System.out.println(dp[n][99]);
        }
    }
}