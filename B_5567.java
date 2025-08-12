import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.ArrayList;
import java.util.StringTokenizer;

public class Main {
    public static boolean[] visited;
    public static void put(ArrayList<ArrayList<Integer>> graph,int x, int y){
        graph.get(x).add(y);
        graph.get(y).add(x);
    }

    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        String str = br.readLine();

        int n = Integer.parseInt(str);

        str = br.readLine();
        int m = Integer.parseInt(str);

        ArrayList<ArrayList<Integer>> graph = new ArrayList<ArrayList<Integer>>();

        ArrayList<Integer> near = new ArrayList<Integer>();

        for (int i = 0; i < n+1; i++) {
            graph.add(new ArrayList<Integer>());
        }

        int ans = 0;
        visited = new boolean[n+1];
        visited[1]=true;
        for (int i = 0; i < m; i++) {
            str = br.readLine();
            StringTokenizer st = new StringTokenizer(str);
            int a = Integer.parseInt(st.nextToken());
            int b = Integer.parseInt(st.nextToken());
            if (a==1){
                near.add(b);
                ans+=1;
                visited[b]=true;
            }
            put(graph, a, b);
        }

        for (int i = 0; i < near.size(); i++) {
            int t = near.get(i);
            for (int j = 0; j < graph.get(t).size(); j++) {
                int tar = graph.get(t).get(j);
                if (visited[tar]==false){
                    visited[tar]=true;
                    ans+=1;
                }
            }
        }

        System.out.println(ans);
    }
}
