import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.StringTokenizer;

public class Main {

    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        String str = br.readLine();
        StringTokenizer st = new StringTokenizer(str);
        int n = Integer.parseInt(st.nextToken());
        int m = Integer.parseInt(st.nextToken());

        int[][] arr = new int[n][m];


        for (int i = 0; i < n; i++) {
            str = br.readLine();
            StringTokenizer st2 = new StringTokenizer(str);
            for (int j = 0; j < m; j++) {
                arr[i][j] = Integer.parseInt(st2.nextToken());
            }
        }

        str = br.readLine();
        int t = Integer.parseInt(str);


        for (int i = 0; i < t; i++) {
            str = br.readLine();
            StringTokenizer st3 = new StringTokenizer(str);

            int ii = Integer.parseInt(st3.nextToken());
            int jj = Integer.parseInt(st3.nextToken());
            int xx = Integer.parseInt(st3.nextToken());
            int yy = Integer.parseInt(st3.nextToken());

            int answer = 0;

            for (int j = ii-1; j < xx; j++) {
                for (int k = jj-1; k < yy; k++) {
                    answer += arr[j][k];
                }
            }
            System.out.println(answer);
        }
    }
}
