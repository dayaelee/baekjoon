import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.HashSet;
import java.util.Set;
import java.util.StringTokenizer;

public class B_26069 {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        String str = br.readLine();

        int n = Integer.parseInt(str);

        Set<String> set = new HashSet<String>();

        for (int i = 0; i < n; i++) {
            str = br.readLine();
            StringTokenizer st = new StringTokenizer(str);
            String a = st.nextToken();
            String b = st.nextToken();

            if (a.equals("ChongChong")){
                set.add(b);

            }else if (b.equals("ChongChong")){
                set.add(a);
            }

            if (set.contains(a)){
                set.add(b);
            }else if (set.contains(b)){
                set.add(a);
            }
        }

        System.out.println(set.size());
    }
}
