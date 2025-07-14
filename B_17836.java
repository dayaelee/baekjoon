import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.*;

class Point {
    public int x, y, sord, time;
    Point(int y, int x, int sord, int time){
        this.y = y;
        this.x = x;
        this.sord = sord;
        this.time = time;
    }
}

public class Main {
    static int[] dy = {-1, 1, 0, 0};
    static int[] dx = {0, 0, -1, 1};
    public static int[][] map;
    public static int[][] dp;
    public static int n, m, t;
    public static boolean[][][] visited;
    public static int answer=Integer.MAX_VALUE;
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        String str = br.readLine();

        StringTokenizer st = new StringTokenizer(str);
        n = Integer.parseInt(st.nextToken());
        m = Integer.parseInt(st.nextToken());
        t = Integer.parseInt(st.nextToken());
        map = new int[n][m];
        dp = new int[n][m];
        visited = new boolean[n][m][2];

        for (int i = 0; i < n; i++) {
            str = br.readLine();
            st = new StringTokenizer(str);
            for (int j = 0; j < m; j++) {
                map[i][j] = Integer.parseInt(st.nextToken());
                dp[i][j]=Integer.MAX_VALUE;
            }
        }

        bfsBasic();
//        System.out.println("hi "+answer);
        if (answer==Integer.MAX_VALUE){
            System.out.println("Fail");
        } else {
            System.out.println(answer);
        }


    }

    public static int bfsBasic() {
        Deque<Point> q = new LinkedList<>();
        q.offer(new Point(0, 0, 0, 0));
        visited[0][0][0]=true;

        while (!q.isEmpty()) {
            Point tmp = q.poll();

//            System.out.println("!!!"+tmp.y +" "+tmp.x+" "+tmp.sord+" "+tmp.time);

            if (tmp.y == n - 1 && tmp.x == m - 1) {
                if (tmp.time <= t) {
                    answer=Math.min(answer, tmp.time);
                }else{
                    continue;
                }
            }

            if (map[tmp.y][tmp.x] == 2) {
                tmp.sord = 1;
            }

            for (int i = 0; i < 4; i++) {
                int ny = tmp.y + dy[i];
                int nx = tmp.x + dx[i];

                if (0 <= ny && ny < n && 0 <= nx && nx < m) {
                    if (map[ny][nx]==1){
                        if (tmp.sord == 1){
                            if (visited[ny][nx][1]==false) {

                                    visited[ny][nx][1] = true;
                                    q.addLast(new Point(ny, nx, 1, tmp.time + 1));

                            }

                        }
                    }else {
                        if (map[ny][nx] == 0 || map[ny][nx]==2) {

                                if (tmp.sord==1){
                                    if(visited[ny][nx][1]==false) {
                                        visited[ny][nx][1] = true;
                                        q.addLast(new Point(ny, nx, 1, tmp.time + 1));
                                    }
                                }else{
                                    if(visited[ny][nx][0]==false) {
                                        visited[ny][nx][0] = true;
                                        q.addLast(new Point(ny, nx, 0, tmp.time + 1));
                                    }
                                }

                        }
                    }
                }
            }
        }
        return -1;
    }
}