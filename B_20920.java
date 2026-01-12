import java.io.*;
import java.util.*;
public class Main {
    public static int n, m;
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        String str = br.readLine();

        StringTokenizer st = new StringTokenizer(str);
        n = Integer.parseInt(st.nextToken());
        m = Integer.parseInt(st.nextToken());

        HashMap<String, Integer> hm = new HashMap<>();        

        for (int i = 0; i<n; i++){
            str = br.readLine();
            if(str.length()>=m){
                if (hm.containsKey(str)){
                    hm.put(str, hm.get(str)+1);
                }else{
                    hm.put(str, 1);
                }
            }
        }

        List<String> keySet = new ArrayList<>(hm.keySet());
        keySet.sort((o1, o2) -> {

            int freqDiff = hm.get(o2) - hm.get(o1);
            if (freqDiff != 0) return freqDiff;

            int lenDiff = o2.length() - o1.length();
            if (lenDiff != 0) return lenDiff;

            return o1.compareTo(o2);
        });


        StringBuilder sb = new StringBuilder();

        for(String key: keySet){
            sb.append(key+"\n");
        }

        System.out.print(sb);
    }
    
}
