import javax.swing.text.View;
import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.StringTokenizer;

public class Main {

    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        String str = br.readLine();

        StringTokenizer st = new StringTokenizer(str);
        int a = Integer.parseInt(st.nextToken());
        int b = Integer.parseInt(st.nextToken());
        int d = Integer.parseInt(st.nextToken());

        boolean[] visited = new boolean[b+1];
        visited[0]=true;
        visited[1]=true;

        for (int i = 2; i < b+1; i++) {
            for (int j = i; j < b+1; j+=i) {
                if (i!=j){
                    visited[j] = true;
//                    System.out.println(j);
                }
            }
//            System.out.println();
        }
        int answer=0;

        String target = Integer.toString(d);
        for (int i = a; i <= b; i++) {
            if (!visited[i]){
                String tmp = Integer.toString(i);
                if (tmp.contains(target)){
                    answer+=1;
                }
            }
        }
        System.out.println(answer);

    }
}