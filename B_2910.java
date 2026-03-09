import java.util.*;
import java.io.*;

public class Main {
    static class Message implements Comparable<Message>{
        int key;
        int value;
        Message(int key, int value){
            this.key = key;
            this.value = value;
        }

        @Override
        public int compareTo(Message o){
            return o.value-value;
        }
    }
    
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        String tmp = br.readLine();

        StringTokenizer st = new StringTokenizer(tmp);
        int n = Integer.parseInt(st.nextToken());
        int c = Integer.parseInt(st.nextToken());

        tmp = br.readLine();

        String[] tmpArr = tmp.split(" ");

        int[] intArr= Arrays.stream(tmpArr).mapToInt(Integer::parseInt).toArray();

        Map<Integer, int[]> map = new LinkedHashMap<>();
        for(int i = 0; i<n; i++){
            if(!map.containsKey(intArr[i])){
                map.put(intArr[i], new int[]{1});
            }else{
                map.get(intArr[i])[0]++; 
            }
        }

        List<Message> list = new ArrayList<>();

        for(Integer key: map.keySet()){
            int[] info = map.get(key);

            list.add(new Message(key, info[0]));
        }

        Collections.sort(list);

        StringBuilder sb = new StringBuilder();

        for(Message m: list){
            for(int i = 0; i<m.value; i++){
                sb.append(m.key+" ");
            }
        }

        System.out.println(sb.toString());

        
    }
    
}
