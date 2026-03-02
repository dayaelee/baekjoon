import java.util.*;
import java.io.*;
public class Main {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));
        String str = br.readLine();

        int n = Integer.parseInt(str);

        String[] arr = new String[n];

        for(int i = 0; i<n; i++){
            String value = br.readLine();
            arr[i] = value;
        }

        Set<String> set = new HashSet<>(Arrays.asList(arr));

        String[] resultArr = set.toArray(new String[0]);

        Arrays.sort(resultArr, new Comparator<String>(){
            @Override
            public int compare (String o1, String o2){
                if(o1.length() == o2.length())
                    return o1.compareTo(o2);
                return o1.length() - o2.length();
            }
        });

        for(int i = 0; i<resultArr.length; i++){
            bw.write(resultArr[i] + "\n");
        }

        bw.flush();


        
    }
    
}
