import java.util.*;
import java.io.*;
public class Main {
    public static int N;
    public static int[][] graph;
    public static int[][] costnow;
    public static int INF = Integer.MAX_VALUE;
    public static boolean visited[][];
    public static int round;
    
    public static int[] dy = {-1, 1, 0, 0};
    public static int[] dx = {0, 0, -1, 1};

    static class Node{
        int y;
        int x;
        int cost;
        public Node(int y, int x, int cost){
            this.y = y;
            this.x = x;
            this.cost = cost;
        }
    }

    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        round=0;
        while(true){
            String str = br.readLine();
            N = Integer.parseInt(str);
            
            if (N>0){
                round+=1;
                graph = new int[N][N];
                for(int i = 0; i<N; i++){
                    str = br.readLine();
                    StringTokenizer st = new StringTokenizer(str);
                    
                    for(int j = 0; j<N; j++){
                        graph[i][j] = Integer.parseInt(st.nextToken());
                    }
                }

                costnow = new int[N][N];
                for(int i = 0; i<N; i++){
                    for(int j = 0; j<N; j++){
                        costnow[i][j]=INF;
                    }
                }
                dijkstra(0, 0);
            }else{
                break;
            }
        }

    }

    public static void dijkstra(int y, int x){
        PriorityQueue<Node> q = new PriorityQueue<> ((o1, o2)-> o1.cost - o2.cost);
        q.add(new Node(y, x, graph[y][x]));
        costnow[y][x]=graph[y][x];
        visited=new boolean[N][N];

        while(!q.isEmpty()){
            Node now = q.poll();
            if(!visited[now.y][now.x]){
                visited[now.y][now.x] = true;
            }

            for(int i = 0; i<4; i++){
                int ny = now.y+dy[i];
                int nx = now.x+dx[i];

                if (0<=nx && nx<N && 0<=ny && ny<N){
                    if (!visited[ny][nx] && costnow[ny][nx]>costnow[now.y][now.x]+graph[ny][nx]){
                        costnow[ny][nx]=costnow[now.y][now.x]+graph[ny][nx];
                        q.add(new Node(ny, nx, costnow[ny][nx]));
                    }
                }
            }
        }
        System.out.println("Problem "+ round+": "+costnow[N-1][N-1]);
    }
}
