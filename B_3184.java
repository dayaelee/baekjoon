import java.io.*;
import java.util.*;

public class Main {
    public static int[] dy = {-1, 1, 0, 0};
    public static int[] dx = {0, 0, -1, 1};

    public static int r, c;
    public static char[][] graph;
    public static boolean[][] visited;
    public static int v, o;

    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        String str = br.readLine();

        StringTokenizer st = new StringTokenizer(str);

        r = Integer.parseInt(st.nextToken());
        c = Integer.parseInt(st.nextToken());

        graph = new char[r][c];
        visited = new boolean[r][c];

        for(int i = 0; i<r; i++){
            str = br.readLine();
            for(int j = 0; j<c; j++){
                graph[i][j]=str.charAt(j);
            }
        }

        v=0;
        o=0;
        
        for(int i = 0; i<r; i++){
            for(int j = 0; j<c; j++){
                if ((graph[i][j]=='.' || graph[i][j]=='v' || graph[i][j]=='o')&&visited[i][j]==false)
                    bfs(i, j);
            }
        }

        System.out.println(o+" "+v);
    }

    public static void bfs(int i, int j){
        Queue<int []> q = new ArrayDeque<>();
        q.offer(new int[]{i, j});
        visited[i][j]=true;

        int vv=0;
        int oo=0;

        while(!q.isEmpty()){
            int[] curr=q.poll();
            int y = curr[0];
            int x = curr[1];

            if(graph[y][x]=='v')
                vv+=1;

            if(graph[y][x]=='o')
                oo+=1;

            for(int l = 0; l<4; l++){
                int ny = y+dy[l];
                int nx = x+dx[l];

                if(0<=ny&& ny<r && 0<=nx && nx<c && visited[ny][nx]==false){
                    if(graph[ny][nx]!='#'){
                        visited[ny][nx]=true;
                        q.offer(new int[]{ny, nx});
                    }
                }
            }

        }

        if (vv>=oo){
            v+=vv;
        } else if (vv<oo){
            o+=oo;
        }

    }
    
}
