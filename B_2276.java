import java.io.*;
import java.util.HashMap;
import java.util.StringTokenizer;

public class Main {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));
        int t = Integer.parseInt(br.readLine());

        for (int i = 0; i < t; i++) {
            int n = Integer.parseInt(br.readLine());
            String str = br.readLine();
            StringTokenizer st = new StringTokenizer(str);
            HashMap<Integer, Integer> note1 = new HashMap<Integer, Integer>();
            for (int j = 0; j < n; j++) {
                note1.put(Integer.parseInt(st.nextToken()), 0);
            }

            int m = Integer.parseInt(br.readLine());
            String str2 = br.readLine();
            StringTokenizer st2 = new StringTokenizer(str2);

            for (int j = 0; j < m; j++) {
                if (note1.containsKey(Integer.parseInt(st2.nextToken()))){
                    bw.write(1+"\n");
                }else {
                    bw.write(0+"\n");
                }
            }
        }
        bw.flush();
        bw.close();
    }
}