import java.util.*;
import java.io.*;

public class Main {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        String str = br.readLine();

        int n = Integer.parseInt(str);

        String tmp = br.readLine();
        String[] numbers = tmp.split(" ");
        
        int[] intArray = Arrays.stream(numbers)
                            .mapToInt(Integer::parseInt)
                            .toArray();

        int[] tmpArray = Arrays.stream(numbers)
                            .mapToInt(Integer::parseInt)
                            .toArray();

        
        HashMap<Integer, Integer> hm = new HashMap<>();

        Arrays.sort(intArray);

        int cnt = 0;
        int value = intArray[0];

        for(int i = 0; i<n; i++){
            if(i != 0){
                if (intArray[i]!=value){
                    value = intArray[i];
                    cnt+=1;
                }
            }
            hm.put(value, cnt);
        }                   

        StringBuilder sb = new StringBuilder();
        for(int i = 0; i<n; i++){
            int key = tmpArray[i];
            sb.append(hm.get(key)+" ");
        }

        System.out.println(sb.toString());

    }
    
}
