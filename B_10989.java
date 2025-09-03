public class B_10989 {
    
}
import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;

public class Main {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        String str = br.readLine();
        int n = Integer.parseInt(str);

        int [] arr = new int[10001];

        for (int i = 0; i < n; i++) {
            str = br.readLine();
            int inputValue = Integer.parseInt(str);
            arr[inputValue]+=1;

        }

        StringBuilder sb = new StringBuilder("");
        for (int i = 0; i < 10001; i++) {
            if (arr[i]>=1){
                for (int j = 0; j < arr[i]; j++) {
                    sb.append(i+"\n");
                }
            }
        }
        System.out.println(sb);
    }
}

