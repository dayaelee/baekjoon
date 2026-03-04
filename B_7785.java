import java.io.*;
import java.util.*;

public class Main {

    static class Member{
        String name;
        String status;
        
        Member(String name, String status){
            this.name = name;
            this.status = status;
        }

    }
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        String tmp = br.readLine();

        int n = Integer.parseInt(tmp);

        Member[] members = new Member[n];
        HashMap<String, String> map = new HashMap<>();

        for(int i = 0; i<n; i++){
            String tmp2 = br.readLine();
            StringTokenizer st = new StringTokenizer(tmp2);
            String key = st.nextToken();
            if (map.containsKey(key)){
                map.replace(key, st.nextToken());
            } else{
                map.put(key, st.nextToken());
            }
        }

        List<String> answer = new ArrayList<>();

        for(String key : map.keySet()){
            if(map.get(key).equals("enter")){
                answer.add(key);
            }
        }

        Collections.sort(answer, Collections.reverseOrder());

        for(String value: answer){
            System.out.println(value);
        }
    }
    
}
