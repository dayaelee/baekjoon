import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.StringTokenizer;

public class Main {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        String str = br.readLine();

        int n, m;
        StringTokenizer st = new StringTokenizer(str);
        n = Integer.parseInt(st.nextToken());
        m = Integer.parseInt(st.nextToken());

        int[] lecture = new int[n];
        String str2 = br.readLine();
        st = new StringTokenizer(str2);
        for (int i = 0; i < n; i++) {
            lecture[i] = Integer.parseInt(st.nextToken());
        }
        int start = 0, end = 0, answer = 0;
        for (int i = 0; i < n; i++) {
            start = Math.max(start, lecture[i]);
            end+=lecture[i];
        }

        int cnt, mid;
        while (start <= end) {
            mid = (start + end) / 2;
            cnt = 1;
            int summ = 0;
            for (int i = 0; i < n; i++) {
                if (summ + lecture[i]>mid){
                    cnt+=1;
                    summ=0;
                }
                summ +=lecture[i];
            }
            if (cnt<=m){
                answer = mid;
                end = mid-1;
            } else{
                start = mid +1;
            }
        }

        System.out.println(answer);
    }
}