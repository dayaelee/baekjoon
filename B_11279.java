import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.Collections;
import java.util.PriorityQueue;

public class Main {

    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        String str = br.readLine();

        int n = Integer.parseInt(str);
        PriorityQueue<Integer> pQ = new PriorityQueue<>(Collections.reverseOrder());
        for (int i = 0; i < n; i++) {
            str = br.readLine();
            int value = Integer.parseInt(str);
            if (value > 0){
                pQ.add(value);
            }else if(value == 0){
                if (pQ.isEmpty()){
                    System.out.println(0);
                }else {
                    System.out.println(pQ.poll());
                }
            }

        }
    }
}
