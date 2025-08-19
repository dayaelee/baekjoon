import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.HashMap;
import java.util.HashSet;
import java.util.Set;
import java.util.StringTokenizer;

public class B_10546 {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        String str = br.readLine();

        int n = Integer.parseInt(str);

        HashMap<String, Integer> map = new HashMap<>();

        for (int i = 0; i < n; i++) {
            str = br.readLine();
            if (map.containsKey(str)){
                map.put(str, map.get(str)+1);
            }else {
                map.put(str, 1);
            }
        }

        for (int i = 0; i < n - 1; i++) {
            str = br.readLine();
            if (map.containsKey(str)){
                map.put(str, map.get(str)-1);
            }
        }

        for (String k: map.keySet()) {
            if (map.get(k)>=1){
                System.out.println(k);
            }
        }
    }
}
