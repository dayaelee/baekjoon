import java.io.*;
import java.util.*;

public class Main {

    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        String tmp = br.readLine();

        int n = Integer.parseInt(tmp);

        Set<String> set = new HashSet();

        for(int i = 0; i<n; i++){
            StringTokenizer st = new StringTokenizer(br.readLine());
            String key = st.nextToken();
            String status = st.nextToken();
            if(status.equals("enter"))
                set.add(key);
            else{
                set.remove(key);
            }
        }

        String[] answer = set.toArray(new String[set.size()]);

        Arrays.sort(answer, (o1, o2)->o2.compareTo(o1));

        for(String value: answer){
            System.out.println(value);
        }
    }
    
}
