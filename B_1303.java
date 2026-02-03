import java.io.*;
import java.util.*;

public class Main {

    public static int[] dy={ -1, 1, 0, 0};
    public static int[] dx={0, 0, -1, 1};

    public static int m, n;
    public static boolean[][] visited;
    public static char[][] graph;



    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        String str = br.readLine();

        StringTokenizer st = new StringTokenizer(str);

        n = Integer.parseInt(st.nextToken());
        m = Integer.parseInt(st.nextToken());

        graph = new char[m][n];


        for(int i = 0; i<m; i++){
            str = br.readLine();
            for(int j = 0; j<n; j++){
                graph[i][j] = str.charAt(j);
            }
        }

        visited = new boolean[m][n];

        int w_cnt =0;
        int b_cnt =0;
        for(int i = 0; i<m; i++){
            for(int j = 0; j<n; j++){
                if(visited[i][j]==false && graph[i][j]=='W'){
                    w_cnt += bfs(i, j, 1);
                }else if (visited[i][j]==false && graph[i][j]=='B'){
                    b_cnt += bfs(i, j, 0);
                }
            }
        }
        System.out.println(w_cnt+" "+b_cnt);
    }

    public static int bfs(int sy, int sx, int check){
        Queue<int []> q = new ArrayDeque<>();
        q.offer(new int[]{sy, sx});
        visited[sy][sx]=true;
        int cnt =0;

        while(!q.isEmpty()){
            int[] curr = q.poll();
            int y = curr[0];
            int x = curr[1];
            cnt+=1;

            for(int i = 0; i<4; i++){
                int ny = y + dy[i];
                int nx = x + dx[i];

                if (0<=ny && ny<m && 0<=nx && nx<n && visited[ny][nx] == false){
                    if(check == 1 && graph[ny][nx]=='W'){
                        visited[ny][nx]=true;
                        q.offer(new int[]{ny, nx});
                    } else if (check == 0 && graph[ny][nx]=='B'){
                        visited[ny][nx]=true;
                        q.offer(new int[]{ny, nx});
                    }
                }
            }


        }
        // System.out.println(cnt*cnt+" ??: "+cnt);
        return cnt*cnt;
        
    }
    
}
