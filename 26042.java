import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.LinkedList;
import java.util.Queue;
import java.util.StringTokenizer;

public class Main {

    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        String str = br.readLine();
        int n = Integer.parseInt(str);

        Queue<Integer> q = new LinkedList<>();

        int maxValue = 0;
        int answer = Integer.MAX_VALUE;

        for (int i = 0; i < n; i++) {
            str = br.readLine();
            StringTokenizer st = new StringTokenizer(str);
            int o = Integer.parseInt(st.nextToken());

            if (o==1){
                int v = Integer.parseInt(st.nextToken());
                q.add(v);
//                System.out.println("qSize: "+ q.size() +" maxValue: "+maxValue);
                if (maxValue==q.size()){
                    answer = Math.min(v, answer);
//                    System.out.println("answer "+ answer + " maxValue: "+ maxValue );
                }else if(maxValue < q.size()){
                    maxValue=q.size();
                    answer = v;
                }
            }else {
                if (!q.isEmpty()) {
                    q.remove();
                }
            }
        }

        System.out.println(maxValue+" "+answer);
    }
}

