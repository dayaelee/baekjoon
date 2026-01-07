import java.util.*;
import java.io.*;

public class Main {
    public static int L, R, C;
    public static char[][][] board;
    public static boolean[][][] visited; 
    public static int Sl, Sr, Sc;
    public static int El, Er, Ec;
    public static int answer;

    public static int[] dh = {0, 0, 0, 0, 1, -1};
    public static int[] dy = {0, 0, 1, -1, 0, 0};
    public static int[] dx = {1, -1, 0, 0, 0, 0};

    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        
        // L, R, C가 0, 0, 0 이 나오지 않는 이상 이건 반복됨 
        while(true){
            String str = br.readLine();

            StringTokenizer st = new StringTokenizer(str);
            L = Integer.parseInt(st.nextToken());
            R = Integer.parseInt(st.nextToken());
            C = Integer.parseInt(st.nextToken());

            if(L==0 && R==0 && C==0){
                break;
            }

            board = new char[L][R][C];

            for(int i = 0; i<L; i++){
                for(int j = 0; j<R; j++){
                    str = br.readLine();
                    board[i][j] = str.toCharArray();
                    for (int k = 0; k<C; k++){
                        if (board[i][j][k]=='S'){
                            Sl = i;
                            Sr = j;
                            Sc = k;
                        } else if (board[i][j][k]=='E'){
                            El = i;
                            Er = j;
                            Ec = k;
                        }
                    }
                }
                str = br.readLine(); // 공백 받기 위함 
            }

            visited = new boolean[L][R][C];
            answer = bfs(Sl, Sr, Sc, El, Er, Ec);
            
            StringBuilder sb = new StringBuilder();
            if (answer==0){
                sb.append("Trapped!");
            }else{
                sb.append("Escaped in ").append(answer).append(" minute(s).");
            }
            System.out.println(sb.toString());
        }
    }

    public static int bfs(int sl, int sr, int sc, int el, int er, int ec){
        int time=0;
        Queue<int []> q = new ArrayDeque<>();
        q.offer(new int[]{sl, sr, sc, 0});
        visited[sl][sr][sc]=true;

        while(!q.isEmpty()){
            int[] cur = q.poll();
            int ch = cur[0];
            int cy = cur[1];
            int cx = cur[2];
            int cm = cur[3];

            if(ch==el && cy==er && cx==ec){
                return cm;
            }
        
            for(int i = 0; i < 6; i++){
                int nh = ch + dh[i];
                int ny = cy + dy[i];
                int nx = cx + dx[i];

                if (0<=nh && nh<L && 0<=ny && ny<R && 0<=nx && nx<C && (board[nh][ny][nx]=='.'|| board[nh][ny][nx]=='E' )){
                    if(visited[nh][ny][nx]==false){
                        visited[nh][ny][nx]=true;
                        q.offer(new int[]{nh, ny, nx, cm+1});
                    }
                }
            }
        }
        return time;
    }
    
}
