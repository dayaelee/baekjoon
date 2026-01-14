import java.util.*;
import java.io.*;

public class Main {
    public static HashMap<String, Integer> hm;
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        String str = br.readLine();

        int n = Integer.parseInt(str);
        int answer = 0;

        hm = new HashMap<String, Integer>();

        for(int i = 0; i<n; i++){
            str = br.readLine();
            if (str.equals("ENTER")){
                hm = new HashMap<String, Integer>();
            }else{
                if(hm.containsKey(str)){
                    hm.put(str, hm.get(str)+1);
                }else{
                    hm.put(str, 1);
                    answer+=1;
                }
            }
        }
        System.out.println(answer);
    }
    
}
