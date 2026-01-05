import java.io.*;
import java.util.*;


public class Main {
    public static int C, N;
    public static ArrayList<ArrayList<Integer>> cost;
    public static int[] dp;
    public static int[][] total;
    public static int INF = Integer.MAX_VALUE;
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        String str = br.readLine();


        StringTokenizer st = new StringTokenizer(str);
        C = Integer.parseInt(st.nextToken());
        N = Integer.parseInt(st.nextToken());

        cost = new ArrayList<>();
        int maxPeople = 0;
        for (int i = 0; i<N; i++){
            ArrayList<Integer> tmp = new ArrayList<>();
            str = br.readLine();
            st = new StringTokenizer(str);

            int c =Integer.parseInt(st.nextToken());
            tmp.add(c); // 비용
            int p =Integer.parseInt(st.nextToken());
            tmp.add(p); // + 사람
            maxPeople = Math.max(maxPeople, p);

            cost.add(tmp);
        }

        dp= new int[maxPeople+C+1];
        Arrays.fill(dp, INF);
        dp[0]=0;
        
        for(int j = 0; j<N; j++){

            int c = cost.get(j).get(0);
            int p = cost.get(j).get(1);

            for (int i = p; i<=maxPeople+C; i++){
                if (dp[i - p] != INF) {
                    dp[i] = Math.min(dp[i], dp[i-p] + c);
                }
            }
        }
        int ans = 1_000_000_000;

        for (int i = C; i<=maxPeople+C; i++){
            ans = Math.min(ans, dp[i]);
        }
        System.out.println(ans);
    }
}
