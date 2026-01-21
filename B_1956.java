import java.io.*;
import java.util.*;

public class Main {
    public static int v, e;
    public static int[][] arr;
    public static int INF = Integer.MAX_VALUE;
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        String str = br.readLine();


        

        StringTokenizer st = new StringTokenizer(str);
        v = Integer.parseInt(st.nextToken());
        e = Integer.parseInt(st.nextToken());

        arr = new int[v+1][v+1];

        

        for(int i = 1; i<=v; i++){
            Arrays.fill(arr[i], INF);
        }

        for(int i = 0; i<e; i++){
            str = br.readLine();
            st = new StringTokenizer(str);
            int a = Integer.parseInt(st.nextToken());
            int b = Integer.parseInt(st.nextToken());
            int c = Integer.parseInt(st.nextToken());

            arr[a][b]=c;
        }


        for(int k = 1; k<=v ; k++){
            for(int i = 1; i<=v; i++){
                for(int j = 1; j<=v; j++){
                    if(arr[i][k]==INF|| arr[k][j]==INF) continue;
                    else{
                        arr[i][j] = Math.min(arr[i][j], arr[i][k]+arr[k][j]);
                    }
                }
            }
        }

        int answer = INF;
        for(int k = 1; k<=v ; k++){
            answer = Math.min(answer, arr[k][k]);
        }

        if (answer == INF){
            System.out.println(-1);
        }else{
            System.out.println(answer);
        }

        
        
    }
    
}
