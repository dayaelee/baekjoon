import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.Arrays;
import java.util.Collections;

public class Main {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        String str = br.readLine();
        int n = Integer.parseInt(str);
        int[] arr = new int[n];
        for (int i = 0; i < n; i++) {
            String str2 = br.readLine();
            arr[i]=Integer.parseInt(str2);
        }
        long answer =0;
        if (n<=2){
            for (int i = 0; i < n; i++) {
                answer+=arr[i];
            }
        }else{
            Arrays.sort(arr);
            int cnt = n-1;
            while (true){
                if ((cnt+1)-3>=0) {
                    answer += arr[cnt];
                    answer += arr[cnt - 1];
                    cnt= cnt-3;
//                    System.out.println("cnt:  "+cnt+" answer: "+answer);
                }else{
                    for (int i = 0; i <= cnt; i++) {
                        answer+=arr[i];
                    }
                    break;
                }
            }
        }
        System.out.println(answer);
    }
}