import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.Arrays;
import java.util.StringTokenizer;

public class Main {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        String str = br.readLine();

        int n = Integer.parseInt(str);

        long[] arr = new long[n];
        String str2 = br.readLine();
        StringTokenizer st = new StringTokenizer(str2);
        for (int i = 0; i < n; i++) {
            arr[i] = Long.parseLong(st.nextToken());
        }

        Arrays.sort(arr);
        long answer = 0;
        if (n == 1){
            System.out.println(arr[0]);
        } else if (n%2==0) {
            int start = 0;
            int end = n-1;
            while (start<end){
                answer = Math.max(answer, arr[start]+arr[end]);
                start+=1;
                end-=1;
            }
        } else {
            int start = 0;
            int end = n-2;
            answer = arr[n-1];
            while (start<end){
                answer = Math.max(answer, arr[start]+arr[end]);
                start+=1;
                end-=1;
            }
        }
        System.out.println(answer);
    }
}