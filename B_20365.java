import java.io.BufferedReader;
import java.io.InputStreamReader;

public class B_20365 {
    public static void main(String[] args) throws Exception {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        int n = Integer.parseInt(br.readLine());
        String str = br.readLine();
        String[] txt = str.split("");

        int b = 0, r = 0, bc = 0, rc = 0;

        if (txt[0].equals("B")) {
            b += 1;
            bc+=1;
        } else {
            r += 1;
            rc+=1;
        }

        for (String s : txt) {
            if (b == 1 && s.equals("B")) {
                continue;
            } else if (b == 1 && s.equals("R")) {
                b = 0;
                r = 1;
                rc += 1;
            } else if (r == 1 && s.equals("R")) {
                continue;
            } else if (r == 1 && s.equals("B")) {
                b = 1;
                r = 0;
                bc += 1;
            }
        }
        System.out.println(Math.min(bc, rc) + 1);
    }
}