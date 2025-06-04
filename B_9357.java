import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.ArrayList;
import java.util.Arrays;
import java.util.HashMap;

public class B_9357 {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));

        int t = Integer.parseInt(br.readLine());

        for (int i = 0; i < t; i++) {

            HashMap<String, ArrayList<String>> h1 = new HashMap<>();

            int n = Integer.parseInt(br.readLine());
//            ArrayList<String> list = new ArrayList<String>();

            for (int j = 0; j < n; j++) {
                String str = br.readLine();
                String[] txt = str.split(" ");

                String key = txt[1];
                String value = txt[0];

                if (!h1.containsKey(key)) {
                    h1.put(key, new ArrayList<String>());
                }

                h1.get(key).add(value);
            }
            int sum=1;
            for (String key : h1.keySet()) {
                sum*=h1.get(key).size()+1;
//                System.out.println(key + "->"+h1.get(key));

            }
            System.out.println(sum-1);

        }



    }
}