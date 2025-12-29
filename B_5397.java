import java.util.*;
import java.io.*;
public class Main {
    public static int N;
    public static ArrayDeque<Character>[] arr;
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        String str = br.readLine();

        N = Integer.parseInt(str);

        arr = new ArrayDeque[N];
        for (int i = 0; i<N; i++){
            arr[i] = new ArrayDeque<Character>();
        }

        for(int i = 0; i<N; i++){
            str = br.readLine();
            // arr[i] ==> A
            // basket ==> B
            ArrayDeque<Character> basket = new ArrayDeque<>();
            for (int j = 0; j<str.length(); j++){
                if (str.charAt(j)=='<'){
                    if(!arr[i].isEmpty()){
                        basket.push(arr[i].pop());
                    }
                } else if (str.charAt(j)=='>'){
                    if (!basket.isEmpty()){
                        arr[i].push(basket.pop());
                    }
                } else if (str.charAt(j)=='-'){
                    if(!arr[i].isEmpty())
                        arr[i].pop();
                }else{
                    arr[i].push(str.charAt(j));
                }
            }
            

            List<Character> list = new ArrayList<>(arr[i]);
            Collections.reverse(list);
            StringBuilder sb = new StringBuilder();
            for (char c : list){
                sb.append(c);
            }

            if (!basket.isEmpty()){
                List<Character> list2 = new ArrayList<>(basket);
                for (char c : list2){
                    sb.append(c);
                }
            }
            String result = sb.toString();
            System.out.println(result);
        }

    }
    
}
