import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.*;

public class Main {

    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        String str = br.readLine();

        int n = Integer.parseInt(str);
        HashMap<String, Integer> h1 = new HashMap<String, Integer>();

        for (int i = 0; i < n; i++) {
            str = br.readLine();
            if (!h1.containsKey(str)) {
                h1.putIfAbsent(str, 1);
            } else{
                h1.replace(str, h1.get(str)+1);
            }
        }


        int maxV = 0;
        String answer="";

        List<Map.Entry<String, Integer>> list = new ArrayList<>(h1.entrySet());
        Collections.sort(list, Map.Entry.comparingByKey());

        LinkedHashMap<String, Integer> sortedMap = new LinkedHashMap<>();
        for (Map.Entry<String, Integer> entry : list){
            sortedMap.put(entry.getKey(), entry.getValue());
        }

        for (Map.Entry<String, Integer> entry : sortedMap.entrySet()){
            int ev = entry.getValue();
            if (maxV<ev){
                maxV=ev;
                answer = entry.getKey();
            }
        }
        System.out.println(answer);
    }
}
