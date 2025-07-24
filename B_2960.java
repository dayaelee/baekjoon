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
        int k = Integer.parseInt(st.nextToken());

        boolean[] visited = new boolean[n+1];
        visited[0] = true;
        visited[1] = true;

        int answer = 0;
        for (int i = 2; i < n+1; i++) {
            for (int j = i; j < n+1; j+=i) {
                if (visited[j]==false) {
                    visited[j] = true;
                    answer += 1;
                    if (answer == k) {
                        System.out.println(j);
                        break;
                    }
                }
            }
        }
    }
}