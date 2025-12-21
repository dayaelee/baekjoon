import java.io.*;
import java.util.*;

public class Main {
    public static Integer N, M;
    public static int[][] graph;
    public static boolean[][] visited;

    public static int[] dy = {-1, 1, 0, 0};
    public static int[] dx = {0, 0, -1, 1};
    public static int t;

    public static Queue<int []> q;

    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        String str = br.readLine();

        StringTokenizer st = new StringTokenizer(str);
        N = Integer.parseInt(st.nextToken());
        M = Integer.parseInt(st.nextToken());

        graph = new int[N][M];

        for(int i = 0; i<N; i++){
            str = br.readLine();
            st = new StringTokenizer(str);
            for(int j = 0; j<M; j++){
                graph[i][j]=Integer.parseInt(st.nextToken());
            }
        }
        
        t=0;
        while (true){
            visited = new boolean[N][M];
           
            bfs(0, 0);

            int check = 0;
            for (int i = 0; i<N; i++){
                for(int j = 0; j<M; j++){
                    if (graph[i][j]>=3){
                        check=1;
                        graph[i][j]=0;
                    }else if (graph[i][j]==2){
                        graph[i][j]=1;
                    }
                }
            }
            if (check>0){
                t+=1;
            }else{
                System.out.println(t);
                break;
            }
        }
    }

    public static void bfs(int sy, int sx){
        q = new ArrayDeque<>();
        q.offer(new int[]{sy, sx});

        while(!q.isEmpty()){
            int[] cur = q.poll();
            int y = cur[0];
            int x = cur[1];

            for (int k = 0; k<4; k++){
                int ny = y+ dy[k];
                int nx = x+ dx[k];// 본인들 주변을 탐색하는데 

                if(0<=ny && ny<N && 0<=nx && nx<M && graph[ny][nx]>=1){ // 공기 닿는곳 
                    graph[ny][nx]+=1;
                }

                if(0<=ny && ny<N && 0<=nx && nx<M && visited[ny][nx]==false && graph[ny][nx]==0){
                    // 큐에 넣기
                    visited[ny][nx]=true;
                    q.offer(new int[]{ny, nx});
                }
            }
        }
        return;
    }
}
