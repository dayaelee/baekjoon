public import java.io.*;
import java.util.*;

public class Main {
    public static int N, M;
    public static int[][] arr;
    public static ArrayList<ArrayList<Integer>> graph;
    public static int[] check;

    public static void putEdge(ArrayList<ArrayList<Integer>> graph, int x, int y){
        graph.get(x).add(y);
    }

    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));

        String str = br.readLine();
        N = Integer.parseInt(str);

        str = br.readLine();
        M = Integer.parseInt(str);

        arr = new int[N+1][N+1];
        graph = new ArrayList<>();
        for(int i = 0; i <= N; i++)
            graph.add(new ArrayList<>()); // 각 노드 별 리스트를 만듦

        StringTokenizer st;
        for(int i = 1; i<=N; i++){
            str = br.readLine();
            st = new StringTokenizer(str);
            
            for(int j = 1; j<=N; j++){
                int value = Integer.parseInt(st.nextToken());
                if (value ==1)
                    arr[i][j]=1;    
            }
        }

        for(int i = 1; i<=N; i++){
            for(int j = 1; j<=N; j++){
                if (arr[i][j]==1){
                    putEdge(graph, i, j);
                }
            }
        }

        str = br.readLine();
        st = new StringTokenizer(str);
        int[] check = new int[M];
        for(int i = 0; i<M; i++)
            check[i]=Integer.parseInt(st.nextToken());

        int answer = 0;

        for(int i = 1; i<M; i++){
            boolean[] visited = new boolean[N+1];
            if (dfs(check[i-1], check[i], visited)!=1){
                answer = 0;
                break;
            }else{
                answer = 1;
            }
        }

        if (answer ==1){
            System.out.println("YES");
        }else{
            System.out.println("NO");
        }

    }
    public static int c = 0;
    public static int dfs(int a, int b, boolean[] visited){

        if (a==b) return 1;
        if (visited[a]) return 0;

        visited[a] = true;

        int n = graph.get(a).size();
        for(int i = 0; i<n; i++){
            c+=1;
            int result = dfs(graph.get(a).get(i), b, visited);
            if (result ==1){
                return 1;
            }
        }
        
        return 0;
    }
}
 {
    
}
