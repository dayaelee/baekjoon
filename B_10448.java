import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.StringTokenizer;

public class Main {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        String str = br.readLine();

        int[] check = new int[1001];
        for (int i = 0; i <50 ; i++) {
            int tmp = (i*(i+1))/2;
            if (tmp <= 1000){
                check[i]=tmp;
            }
        }

        int t = Integer.parseInt(str);
        for (int i = 0; i < t; i++) {
            str = br.readLine();
            int n = Integer.parseInt(str);
            int cnt =44;
            int answer = 0;
            while (cnt>=0) {
                int tmp = n;
                for (int j = cnt; j > 0; j--) {
                    for (int k = j; k > 0; k--) {
                        for (int l = k; l > 0; l--) {
                            tmp = n;
                            if (tmp-check[j]-check[k]-check[l]==0){
                                answer =1;
                                break;
                            }
                        }
                        if (answer == 1){
                            break;
                        }
                    }
                    if (answer == 1){
                        break;
                    }
                }
                if (answer == 1){
                    break;
                }
                cnt--;
            }
            System.out.println(answer);
        }
    }
}

