
import java.awt.Point;
import java.util.*;
import java.io.*;

import static java.lang.Math.abs;

public class Main {
    public static int n, l, r;
    public static int[] dy={1, -1, 0, 0};
    public static int[] dx={0, 0, -1, 1};
    public static boolean[][] visited;
    public static int[][] mapp;
    public static ArrayList<Point> myPocket;
    public static int check = 0;
    public static int day = 0;

    public static void main(String[] args) throws IOException{
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));
        StringTokenizer st = new StringTokenizer(br.readLine(), " ");
        n = Integer.parseInt(st.nextToken());
        l = Integer.parseInt(st.nextToken());
        r = Integer.parseInt(st.nextToken());

        mapp = new int[n][n];
        for(int i = 0; i<n; i++){
            st = new StringTokenizer(br.readLine(), " ");
            for(int j = 0; j<n; j++){
                mapp[i][j] = Integer.parseInt(st.nextToken());
            }
            //System.out.println(Arrays.toString(mapp[i]));
        }
        while (true){
            // 전체를 순회하는
            visited = new boolean[n][n];
            check = 0;
            for(int i = 0; i<n; i++){
                for (int j = 0; j<n; j++){
                    if (visited[i][j] == false){
                        myPocket = bfs(i, j);
                        int cnt = myPocket.size();
                        if (cnt >=2) {
                            check+=1;
                        }
                        //System.out.println("cnt: "+ cnt);

                        int summ=0;
                        for(int k = 0; k<cnt; k++){
                             Point a = myPocket.get(k);
                             summ+=mapp[a.y][a.x];
                             //System.out.println("hi     "+mapp[a.y][a.x]);
                        }
                        for(int k = 0; k<cnt; k++){
                            Point a = myPocket.get(k);
                            mapp[a.y][a.x]= (int)(summ/cnt);
                            //System.out.println(summ/cnt);
                        }
                    }
                }
            }
//            for(int i = 0; i<n; i++){
//                System.out.println(Arrays.toString(mapp[i]));
//            }

            if (check==0){
                break;
            } else{
                day +=1;
            }

        }

        System.out.println(day);

    }

    public static ArrayList<Point> bfs(int i, int j){
        ArrayDeque<Point> q = new ArrayDeque<Point>();
        q.add(new Point(j, i));
        visited[i][j]= true;

        ArrayList<Point> pocket = new ArrayList<Point>();
        pocket.add(new Point(j, i));

        while (!q.isEmpty()){
            Point p = q.pollFirst();

            for (int k = 0; k< 4; k++){
                int ny = p.y + dy[k];
                int nx = p.x + dx[k];

                if (0<= ny && ny<n && 0<=nx && nx<n){
                    if (!visited[ny][nx]){
                        int value = mapp[p.y][p.x];
                        int newValue = mapp[ny][nx];
                        int target = abs(newValue-value);

                        if (target>=l && target<=r){
                            visited[ny][nx]=true;
                            q.add(new Point(nx, ny));
                            pocket.add(new Point(nx, ny));
                        }
                    }
                }
            }
        }
        return pocket;
    }
}