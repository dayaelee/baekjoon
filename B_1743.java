import java.io.*;
import java.util.*;

public class Main {
    public static int[] dy = {-1, 1, 0, 0};
    public static int[] dx = {0, 0, -1, 1};

    public static int n, m, k;
    public static boolean[][] visited;
    public static char[][] graph;
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        String str = br.readLine();

        StringTokenizer st = new StringTokenizer(str);
        n = Integer.parseInt(st.nextToken());
        m = Integer.parseInt(st.nextToken());
        k = Integer.parseInt(st.nextToken());

        graph = new char[n][m];
        for(int i = 0; i<n; i++){
            Arrays.fill(graph[i], '.');
        }

        visited = new boolean[n][m];


        for(int i = 0; i<k; i++){
            str = br.readLine();
            st = new StringTokenizer(str);

            int r = Integer.parseInt(st.nextToken());
            int c = Integer.parseInt(st.nextToken());
            graph[r-1][c-1] = '#';
        }
        int answer = 0;

        for(int i = 0; i<n; i++){
            for(int j = 0; j<m; j++){
                if (visited[i][j]==false && graph[i][j]=='#'){
                    visited[i][j]=true;
                    int tmp = bfs(i, j);
                    answer = Math.max(answer, tmp);
                }
            }
        }

        System.out.println(answer);
    }

    public static int bfs(int sy, int sx){
        Queue<int []> q = new ArrayDeque<>();
        q.offer(new int[]{sy, sx, 0});
        int cnt=1;
        while(!q.isEmpty()){
            int[] cur = q.poll();
            int y = cur[0];
            int x = cur[1];
            // cnt = cur[2];

            for(int i = 0; i<4; i++){
                int ny = y+dy[i];
                int nx = x+dx[i];

                if(0<=ny && ny<n && 0<=nx && nx<m && visited[ny][nx]==false && graph[ny][nx]=='#'){
                    visited[ny][nx]=true;
                    q.offer(new int[]{ny, nx, cnt+1});
                    cnt+=1;
                }
            }
        }
        return cnt;
    }
    
}
