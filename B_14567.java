import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.*;
import java.util.stream.Collectors;

public class Main {

    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        String str = br.readLine();

        StringTokenizer st = new StringTokenizer(str);
        int n = Integer.parseInt(st.nextToken());
        int m = Integer.parseInt(st.nextToken());

        int[] dp = new int[n+1];
        int[] time = new int[n+1];
        for (int i = 0; i < n+1; i++) {
            dp[i]=1;
            time[i]=1;
        }

        ArrayList<ArrayList<Integer>> arr = new ArrayList<>();
        for (int i = 0; i < n+1; i++) {
            arr.add(new ArrayList<>());
        }

        int[] indegree= new int[n+1]; // 진입차수

        for (int i = 0; i < m; i++) {
            str = br.readLine();
            st = new StringTokenizer(str);
            int a = Integer.parseInt(st.nextToken());
            int b = Integer.parseInt(st.nextToken());
            arr.get(a).add(b);
            indegree[b]+=1;
        }

        Queue<Integer> q = new LinkedList<>();

        for (int i = 1; i < n + 1; i++) {
            if (indegree[i]==0){ // 진입차수가 0인것 추가
                q.add(i);
            }
        }

        while(!q.isEmpty()){
            int now = q.poll();
            for (int i = 0; i < arr.get(now).size(); i++) {
                int value = arr.get(now).get(i);
                indegree[value]-=1;
                dp[value] = Math.max(dp[value], dp[now]+time[value]);
                if (indegree[value]==0){
                    q.add(value);
                }
            }
        }

        int[] answer = Arrays.copyOfRange(dp, 1, dp.length);

        String result = Arrays.stream(answer)
                .mapToObj(String::valueOf)
                .collect(Collectors.joining(" "));

        System.out.println(result);
    }
}