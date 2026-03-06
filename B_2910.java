import java.util.*;
import java.io.*;

public class Main {
    static class message implements Comparable<message>{
        int key;
        int value;
        int idx;
        message(int key, int value, int idx){
            this.key = key;
            this.value = value;
            this.idx = idx;
        }

        @Override
        public int compareTo(message o){
            if(value !=o.value)
                return o.value - value;
            return idx - o.idx;
        }
    }
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        String str = br.readLine();

        StringTokenizer st = new StringTokenizer(str);

        int n = Integer.parseInt(st.nextToken());
        int c = Integer.parseInt(st.nextToken());

        String tmp = br.readLine();
        String[] tmpArr = tmp.split(" ");

        int[] numArr = Arrays.stream(tmpArr)
                            .mapToInt(Integer::parseInt)
                            .toArray();

        // 정수 배열 정렬
        // Arrays.sort(numArr);

        Map<Integer, int[]> map = new HashMap<>();
        for(int i = 0; i<numArr.length; i++){
            if (!map.containsKey(numArr[i])){
                map.put(numArr[i], new int[]{1, i});
            }else{
                map.get(numArr[i])[0]++;
            }
        }
        

        List<message> list = new ArrayList<>();
        for (int key : map.keySet()){
            int[] info = map.get(key);
            list.add(new message(key, info[0], info[1]));
        }

        Collections.sort(list);


        StringBuilder sb = new StringBuilder();
        for(message tmpMap: list){   
            for(int i = 0; i<tmpMap.value; i++) 
                sb.append(tmpMap.key+" ");
        }
        

        System.out.println(sb.toString());
    }    
}
