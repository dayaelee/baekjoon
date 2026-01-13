import java.util.*;
import java.io.*;
public class Main {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        String str = br.readLine();

        int n = Integer.parseInt(str);

        HashMap<Long, Integer> hm = new HashMap<>();

        for(int i = 0; i<n; i++){
            str = br.readLine();
            long tmp = Long.parseLong(str);
            if(hm.containsKey(tmp)){
                int value = hm.get(tmp);
                hm.put(tmp, value+1);
            }else{
                hm.put(tmp, 1);
            }
        }

        List<Long> keySet = new ArrayList<>(hm.keySet());
        keySet.sort((o1, o2) -> {
            int freqDiff = hm.get(o2) - hm.get(o1);
            if (freqDiff != 0) return freqDiff;

            return o1.compareTo(o2);

        });
        
        for(Long l: keySet){
            System.out.println(l);
            break;
        }
    }
    
}
