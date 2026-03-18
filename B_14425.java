import java.io.*;
import java.util.*;

public class Main {

    static boolean isExist(String[] tmp, int n, String s){
        int start = 0;
        int end = n-1;
        while(start<=end){
            int mid = (start+end)/2;
            if(tmp[mid].equals(s)){
                return true;
            } else if (tmp[mid].compareTo(s)<0){
                start=mid+1;
            } else if (tmp[mid].compareTo(s)>=0){
                end = mid-1;
            }
        }
        return false;
    }

    public static void main(String[] args) throws IOException  {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));
        String str = br.readLine();

        StringTokenizer st = new StringTokenizer(str);
        int n = Integer.parseInt(st.nextToken());   
        int m = Integer.parseInt(st.nextToken());    


        String[] tmp = new String[n];

        for(int i = 0; i < n; i++){
            tmp[i] = br.readLine();
        }
        Arrays.sort(tmp);
        int cnt=0;
        for(int i = 0; i<m; i++){
            if(isExist(tmp, n, br.readLine()))
                cnt+=1;
        }

        System.out.println(cnt);
        
    }
    
}
