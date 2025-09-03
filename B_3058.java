import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.StringTokenizer;

public class Main {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        String str = br.readLine();

        int t = Integer.parseInt(str);
        for (int i = 0; i < t; i++) {
            str = br.readLine();
            StringTokenizer st = new StringTokenizer(str);
            int sum = 0;
            int minV = Integer.MAX_VALUE;
            for (int j = 0; j < 7; j++) {
                int tmp = Integer.parseInt(st.nextToken());

                if (tmp%2==0){
                    sum+=tmp;
                    minV = Math.min(minV, tmp);
                }
            }
            System.out.println(sum +" "+minV);
        }
    }
}

