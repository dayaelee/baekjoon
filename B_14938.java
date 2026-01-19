import java.util.*;
import java.io.*;


public class Main {
    public static int INF = Integer.MAX_VALUE;
    public static int n, m, r;
    public static int[] items;
    public static int[][] graph;
    public static int maxItem;
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        String str = br.readLine();

        StringTokenizer st = new StringTokenizer(str);

        n = Integer.parseInt(st.nextToken());
        m = Integer.parseInt(st.nextToken());
        r = Integer.parseInt(st.nextToken());

        str = br.readLine();

        items = new int[n+1];
        st = new StringTokenizer(str);
        maxItem = 0;
        for(int i = 1; i<=n; i++){
            items[i]=Integer.parseInt(st.nextToken());
            maxItem = Math.max(maxItem, items[i]);
        }
        
        graph = new int[n+1][n+1];
        for(int i = 0; i<=n; i++){
            Arrays.fill(graph[i], INF);
            graph[i][i]=0;
        }

        for(int i = 0; i<r; i++){
            str = br.readLine();
            st = new StringTokenizer(str); 
            
            int a = Integer.parseInt(st.nextToken());
            int b = Integer.parseInt(st.nextToken());
            int l = Integer.parseInt(st.nextToken());

            graph[a][b] = Math.min(graph[a][b], l);
            graph[b][a] = Math.min(graph[b][a], l);
        }
        
        for(int k = 1; k<=n; k++){
            for(int i = 1; i<=n; i++){
                for(int j = 1; j<=n; j++){
                        if(graph[i][k]== INF || graph[k][j]== INF) continue;
                        graph[i][j] = Math.min(graph[i][j], graph[i][k] + graph[k][j]);
                }
            }
        }

        int answer = 0; 
        int value = 0;
        for(int k = 1; k<=n; k++){ // k 에 떨어졌음. 
            value = 0;
            int check = 0;
            for(int i = 1; i<=n; i++){ 
                if (graph[k][i]>0 && graph[k][i] <= m && graph[i][k] <= m && graph[i][k]>0){
                    if(check == 0){
                        value += items[k];
                        check=1;                        
                    }
                    value += items[i];
                }
            }
            answer = Math.max(value, answer);
        }
        answer = Math.max(maxItem, answer);
        System.out.println(answer);
    }
    
}
