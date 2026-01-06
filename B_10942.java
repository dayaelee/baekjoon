import java.util.*;
import java.io.*;

public class Main {
    public static int N, M;
    public static int[] arr;
    public static int[][] questions;
    public static int[][] board;
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        String str = br.readLine();

        N=Integer.parseInt(str);
        
        arr = new int[N];

        str = br.readLine();
        StringTokenizer st= new StringTokenizer(str);
        for(int i = 0; i<N; i++){
            arr[i]=Integer.parseInt(st.nextToken());
        }

        str = br.readLine();
        M=Integer.parseInt(str);
        questions = new int[M][2];
        for(int i = 0; i<M; i++){
            str = br.readLine();
            st = new StringTokenizer(str);
            questions[i][0] = Integer.parseInt(st.nextToken());
            questions[i][1] = Integer.parseInt(st.nextToken());
        }
        board = new int[N][N];


        // 길이 1
        for (int i = 0; i < N; i++) board[i][i] = 1;

        // 길이 2
        for (int i = 0; i < N - 1; i++) {
            if (arr[i] == arr[i + 1]) board[i][i + 1] = 1;
        }

        // 길이 3 이상
        for (int len = 3; len <= N; len++) {
            for (int i = 0; i + len - 1 < N; i++) {
                int j = i + len - 1;
                if (arr[i] == arr[j] && board[i + 1][j - 1] == 1) {
                    board[i][j] = 1;
                }
            }
        }

        StringBuilder sb = new StringBuilder();

        for(int i = 0; i<M; i++){
            int from = questions[i][0]-1;
            int to = questions[i][1]-1;
            sb.append(board[from][to]).append('\n');
        }
        System.out.println(sb);
    }
    
}
