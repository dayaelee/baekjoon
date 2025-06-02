import java.io.BufferedReader;
import java.io.InputStreamReader;
import java.util.Scanner;
import java.util.StringTokenizer;

public class B_14620 {
    
    public static int cost= Integer.MAX_VALUE;

    public static int[] dy = {1, -1, 0, 0};
    public static int[] dx = {0, 0, -1, 1};
    public static void main(String[] args) throws Exception {
        // Scanner sc = new Scanner(System.in);
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));

        int n = Integer.parseInt(br.readLine());
        
        int[][] mapp = new int[n][n];
        boolean[][] visited = new boolean[n][n];

        for (int i = 0; i<n; i++){
            StringTokenizer st = new StringTokenizer(br.readLine());

            for(int j = 0; j<n; j++){
                int data = Integer.parseInt(st.nextToken());
                mapp[i][j]=data;
            }
        }

        for (int i = 0; i<n; i++){
            for(int j = 0; j<n; j++){
                visited[i][j]=false;
            }
        }
        backtrack(0, 0, mapp, 0, visited, n, 0);
        System.out.println(cost);
    }

    public static void backtrack(int y, int x, int[][] mapp, int cnt, boolean[][] visited, int n, int sum){
        if (cnt==3){
            if (cost>sum){
                cost=sum;
            }
        }
        
        for (int i = 0; i < n; i++) {
            for (int j = 0; j < n; j++) {
                if (visited[i][j]==false){
                    int check = 0;
                    int tmp =0;
                    for (int j2 = 0; j2 < 4; j2++) {
                        int ny = i + dy[j2];
                        int nx = j + dx[j2];
                        if(0<=ny && ny<n && 0<=nx && nx<n && visited[ny][nx]==false){
                            check=1;
                            tmp+=mapp[ny][nx];
                        } else{
                            check=0;
                            tmp=0;
                            break;
                        }
                    }
                    tmp+=mapp[i][j];
                    if (tmp+sum>=cost){
                        tmp=0;
                        check=0;
                        continue;
                    }

                    if (check == 1){
                        visited[i][j]=true;
                        sum+=mapp[i][j];
                        for (int j2 = 0; j2 < 4; j2++) {
                            int ny = i + dy[j2];
                            int nx = j + dx[j2];
                            visited[ny][nx]=true;
                            sum+=mapp[ny][nx];

                        }
                        
                        backtrack(i, j, mapp, cnt+1, visited, n, sum);

                        visited[i][j]=false;
                        sum-=mapp[i][j];

                        for (int j2 = 0; j2 < 4; j2++) {
                            int ny = i + dy[j2];
                            int nx = j + dx[j2];
                            visited[ny][nx]=false;
                            sum-=mapp[ny][nx];
                        }
                    }
                }
            }
        }
    }
}