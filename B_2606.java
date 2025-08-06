import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.*;

public class Main {
    public static int n;
    public static int[][] graph;
    public static boolean[] visited;
    public static int answer;

    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        String str = br.readLine();

        n = Integer.parseInt(str);
        str = br.readLine();
        int m = Integer.parseInt(str);

        graph = new int[n+1][n+1];
        visited = new boolean[n+1];

        for (int i = 0; i < m; i++) {
            str = br.readLine();
            StringTokenizer st = new StringTokenizer(str);
            int a = Integer.parseInt(st.nextToken());
            int b = Integer.parseInt(st.nextToken());

            putEdge(graph, a, b);
            putEdge(graph, b, a);
        }

        answer = 0;
        visited[1]=true;
        dfs(1);
        System.out.println(answer);
    }

    public static void putEdge(int[][] graph, int x, int y){
        graph[x][y] = 1;
    }

    public static void dfs(int start){
        for (int i = 1; i < n+1; i++) {
            if (graph[start][i] == 1 && visited[i] == false) {
                visited[i] = true;
                answer += 1;
                dfs(i);
            }
        }
    }
}
