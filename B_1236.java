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

        char[][] entire = new char[n][m];

        for (int i = 0; i < n; i++) {
            str = br.readLine();
            entire[i] = str.toCharArray();
        }

        int[] rowCheck = new int[n];
        int[] colCheck = new int[m];

        for (int i = 0; i < n; i++) {
            for (int j = 0; j < m; j++) {
                if (entire[i][j]=='X'){
                    rowCheck[i]+=1;
                    break;
                }
            }
        }

        for (int i = 0; i < m; i++) {
            for (int j = 0; j < n; j++) {
                if(entire[j][i]=='X'){
                    colCheck[i]+=1;
                    break;
                }
            }
        }

        int answer1=0;
        int answer2=0;
        for (int i = 0; i < n; i++) {
            if (rowCheck[i]==0){
                answer1+=1;
            }
        }
        for (int i = 0; i < m; i++) {
            if(colCheck[i]==0)
                answer2+=1;
        }

        System.out.println(Math.max(answer1, answer2));
    }
}
