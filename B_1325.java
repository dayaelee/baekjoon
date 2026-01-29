import java.io.*;
import java.util.*;


public class Main {
    public static int n, m;
    public static int [] arr;
    public static ArrayList<Integer>[] graph;
    // public static boolean [] visited;
    public static int[] visited;
    public static int stamp = 1;

    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        String str = br.readLine();

        StringTokenizer st = new StringTokenizer(str);
        n = Integer.parseInt(st.nextToken());
        m = Integer.parseInt(st.nextToken());

        arr = new int[n+1];
        graph = new ArrayList[n+1];
        for(int i = 0; i<=n; i++){
            graph[i] = new ArrayList<Integer>();
        }

        for(int i = 0; i<m; i++){
            str = br.readLine();
            st = new StringTokenizer(str);

            int a = Integer.parseInt(st.nextToken());
            int b = Integer.parseInt(st.nextToken());

            graph[b].add(a);
        }

        Arrays.fill(arr, 1);
        // visited = new boolean[n+1];
        visited = new int[n+1];
        for(int i = 1; i<=n; i++){
            // Arrays.fill(visited, false);
            arr[i]=bfs(i);
        }

        StringBuilder sb = new StringBuilder();
        int maxx=0;
        
        for(int i = 1; i<=n; i++){
            maxx = Math.max(arr[i], maxx);
        }

        for(int i = 1; i<=n; i++){
            if (maxx==arr[i])
                sb.append(i+" ");
        }

        System.out.println(sb.toString());
    }

    public static int bfs(int start){
        Queue<Integer> q = new ArrayDeque<>();
        q.add(start);
        visited[start] = stamp;
        int cnt = 1;

        while(!q.isEmpty()){
            int now = q.poll();
            for (int next: graph[now]){
                if(visited[next]!=stamp){
                    visited[next] = stamp;
                    cnt++;
                    q.add(next);
                }
            }
        }
        stamp++;
        return cnt;
    }
}
