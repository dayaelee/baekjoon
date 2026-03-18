import java.io.*;
import java.util.*;

public class Main {
    public static void main(String[] args) throws IOException  {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));
        String str = br.readLine();

        StringTokenizer st = new StringTokenizer(str);
        int n = Integer.parseInt(st.nextToken());   
        int m = Integer.parseInt(st.nextToken());    


        Set<String> tmp = new HashSet<>();

        for(int i = 0; i<n; i++){
            tmp.add(br.readLine());
        }


        int cnt=0;
        for(int i = 0; i<m; i++){
            if(tmp.contains(br.readLine()))
                cnt+=1;
        }

        System.out.println(cnt);
        
    }
    
}
