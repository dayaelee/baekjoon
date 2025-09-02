import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.ArrayList;
import java.util.List;

public class Main {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        String str = br.readLine();
        int t = Integer.parseInt(str);
        for (int i = 0; i < t; i++) {
            str = br.readLine();
            int n = Integer.parseInt(str);

            int check = 0;
            for (int j = 2; j <= 64; j++) {
                List<Integer> list = new ArrayList<>();
                if (j != 1) {
                    int tmp = n;
                    while(true){
                        if (tmp/j>=0) {
                            list.add(tmp % j);
                            if (tmp/j==0)
                                break;
                            tmp = tmp / j;
                        } else{
                            break;
                        }
                    }
                }

                for (int jjj = 0; jjj < (list.size() / 2); jjj++) {
                    if (list.get(jjj) == list.get(list.size() - jjj - 1)) {
                        check = 1;
                    } else {
                        check = 0;
                        break;
                    }
                }
                if (check == 1)
                    break;
            }
            System.out.println(check);
        }
    }
}

