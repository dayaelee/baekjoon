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

        arr = Arrays.stream(arr).boxed().sorted((Collections.reverseOrder()))
                .mapToInt(Integer::intValue).toArray();

//        for (int i : arr) {
//            System.out.println("hi: "+i);
//        }
        long answer = 0;
        for (int i = 0; i < n; i++) {
//            System.out.println(arr[i]+"???"+i);
            int tmp = arr[i]-i;
            if (tmp>=0){
                answer+=tmp;
            }
        }
        System.out.println(answer);
    }
}