import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;

public class Main {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        String str = br.readLine();

        int[] check = new int[1001];
        for (int i = 0; i <50 ; i++) {
            int tmp = (i*(i+1))/2;
            if (tmp <= 1000)
                check[i]=tmp;
        }

        int t = Integer.parseInt(str);
        for (int i = 0; i < t; i++) {
            str = br.readLine();
            int n = Integer.parseInt(str);
            int answer = 0;
            int tmp = n;
            for (int j = 44; j > 0; j--) {
                for (int k = j; k > 0; k--) {
                    for (int l = k; l > 0; l--) {
                        tmp = n;
                        if (tmp-check[j]-check[k]-check[l]==0){
                            answer =1;
                            break;
                        }
                    }
                    if (answer == 1)
                        break;
                }
                if (answer == 1)
                    break;
            }
            System.out.println(answer);
        }
    }
}

