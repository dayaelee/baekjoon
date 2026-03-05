import java.io.*;
import java.util.*;
public class Main {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        String str = br.readLine();

        int n = Integer.parseInt(str);

        HashMap<String, Integer> hm = new HashMap<>();
        for(int i = 0; i<n; i++){
            String tmp = br.readLine();

            if(hm.containsKey(tmp)){
                hm.put(tmp, hm.get(tmp)+1);
            }else{
                hm.put(tmp, 1);
            }
        }

        List<Map.Entry<String, Integer>> entries = new ArrayList<>(hm.entrySet());


        entries.sort((e1, e2) ->{
            if(e1.getValue()==e2.getValue())
                return e1.getKey().compareTo(e2.getKey());
            return e2.getValue().compareTo(e1.getValue());
        });
        for(Map.Entry<String, Integer> entry :entries){
            System.out.println(entry.getKey());
            break;
            
        }
    }
    

}
