import java.util.*;
import java.io.*;
public class Main {
    public static int n, m;
    public static int[] sDegree;
    public static ArrayList<Integer>[] adj;
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        String str = br.readLine();

        StringTokenizer st = new StringTokenizer(str);
        n = Integer.parseInt(st.nextToken());
        m = Integer.parseInt(st.nextToken());

        sDegree = new int[n+1];
        adj = new ArrayList[n+1];

        for (int i = 1; i<=n; i++){
            adj[i] = new ArrayList<>();
        }

        for(int i = 0; i<m; i++){
            str = br.readLine();
            st = new StringTokenizer(str);
            int a = Integer.parseInt(st.nextToken());
            int b = Integer.parseInt(st.nextToken());

            adj[a].add(b);
            sDegree[b]++;
        }


        PriorityQueue<Integer> pq = new PriorityQueue<>();

        for(int i = 1; i <= n; i++){
            if(sDegree[i] == 0){
                pq.add(i);
            }
        }
        StringBuilder answer = new StringBuilder();

        while(!pq.isEmpty()){
            int now = pq.poll();
            answer.append(now+" ");

            for(Integer next : adj[now]){
                sDegree[next]--;
                if(sDegree[next]==0){
                    pq.add(next);
                }
            }
        }

        System.out.println(answer);


    }
    
}
