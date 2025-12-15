import java.io.*;
import java.util.*;
public class Main {
    public static int M, N;
    public static int[][] arr;
    public static boolean[][] visited;
    public static int[] dy = {-1, -1, -1, 0, 0, 1, 1, 1}; // 좌상, 상, 우상, 좌, 우, 좌하, 하, 우하
    public static int[] dx = {-1, 0, 1, -1, 1, -1, 0, 1}; // 좌상, 상, 우상, 좌, 우, 좌하, 하, 우하
    public static int answer;
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));
        StringTokenizer st = new StringTokenizer(br.readLine());
        M = Integer.parseInt(st.nextToken());
        N = Integer.parseInt(st.nextToken());
        arr = new int[M][N];
        visited = new boolean[M][N];
        for (int i = 0; i<M; i++){
            String tmp = br.readLine();
            st = new StringTokenizer(tmp);
            for (int j = 0; j<N; j++){
                arr[i][j] = Integer.parseInt(st.nextToken());
            }
        }
        // 그냥 전체 순회하고 dfs로 방문처리 
        for (int i = 0; i<M; i++){
            for (int j = 0; j<N; j++){
                if (arr[i][j]==1 && visited[i][j]==false){
                    answer +=1;
                    dfs(i, j);
                    
                }
            }
        }
        System.out.println(answer);
    }
    public static void dfs(int sy, int sx){
        for (int i = 0; i <8; i++){
            int ny = sy + dy[i];
            int nx = sx + dx[i];
            if (ny<0 || ny>=M || nx<0 || nx>=N || visited[ny][nx]==true || arr[ny][nx]==0){
                continue;
            } 
            visited[ny][nx]=true;
            // System.out.println(ny +" "+nx+" ????????");
            dfs(ny, nx);
        }
    }
}
