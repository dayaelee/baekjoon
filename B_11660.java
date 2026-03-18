import java.util.*;
import java.io.*;
public class Main {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));
        String str = br.readLine();
        StringTokenizer st = new StringTokenizer(str);

        int n = Integer.parseInt(st.nextToken());
        int m = Integer.parseInt(st.nextToken());

        int[][] arr = new int[n+1][n+1];
        int[][] nu = new int[n+1][n+1];
        for(int i = 1; i <= n; i++){
            str = br.readLine();
            st = new StringTokenizer(str);
            for(int j = 1; j <= n; j++){
                arr[i][j] = Integer.parseInt(st.nextToken());
                nu[i][j]= nu[i][j-1]+arr[i][j];
            }
        }

        for(int i = 0; i<m; i++){
            int sum = 0;
            str = br.readLine();
            st = new StringTokenizer(str);
            int x1 =Integer.parseInt(st.nextToken());
            int y1 =Integer.parseInt(st.nextToken());
            int x2 =Integer.parseInt(st.nextToken());
            int y2 =Integer.parseInt(st.nextToken());

            for(int k = x1; k<=x2; k++){
                sum+=nu[k][y2]-nu[k][y1-1];
            }
            bw.write(sum+"\n");
        }
        bw.flush();
        bw.close();
    }
}
