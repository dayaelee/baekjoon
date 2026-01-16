import java.io.*;
import java.util.*;

public class Main {
    public static int n, m;
    public static int[] degree;
    public static ArrayList<Integer>[] adj;
    
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        String str = br.readLine();

        StringTokenizer st = new StringTokenizer(str);
        n = Integer.parseInt(st.nextToken());
        m = Integer.parseInt(st.nextToken());

        degree = new int[n+1];
        adj = new ArrayList[n+1];

        for (int i  = 1; i<= n; i++){
            adj[i] = new ArrayList<Integer>();
        }

        for(int i = 0; i<m; i++){
            str = br.readLine();
            st = new StringTokenizer(str);
            int tmp = Integer.parseInt(st.nextToken());
            int start = Integer.parseInt(st.nextToken());
            for(int j = 0; j<tmp-1; j++){
                int value = Integer.parseInt(st.nextToken());
                adj[start].add(value);
                start = value;
                degree[value]+=1;
            }
        }
        int cnt = 0;
        Queue<Integer> pq = new ArrayDeque<>();

        for(int i = 1; i<=n; i++){
            if (degree[i]==0){
                pq.add(i);
            }
        }

        StringBuilder sb = new StringBuilder();
        while(!pq.isEmpty()){
            int now = pq.poll();
            sb.append(now+"\n");
            cnt+=1;
            for(int next:adj[now]){
                degree[next]-=1;
                if(degree[next]==0)
                    pq.add(next);
            }
        }

        if(cnt == n)
            System.out.print(sb);
        else{
            System.out.print(0);
        }
    }
}