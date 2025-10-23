import java.io.*;
import java.util.*;

public class Main {
    public static void main(String[] args) throws IOException{
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));

        String str = br.readLine();

        StringTokenizer st = new StringTokenizer(str);
        
        int n = Integer.parseInt(st.nextToken());
        int m = Integer.parseInt(st.nextToken());

        str = br.readLine();
        int[] arr = new int[n];
        st = new StringTokenizer(str);
        for(int i = 0; i< n; i++){
            arr[i]=Integer.parseInt(st.nextToken());
        }

        int[] a = new int[n];
        for(int i = 0; i<n; i++){
            if (i==0){
                a[i]=arr[i];
            }else{
                a[i]=a[i-1]+arr[i];
            }
        }

        while(m-- >0){
            str = br.readLine();
            st = new StringTokenizer(str);
            int i= Integer.parseInt(st.nextToken());
            int j= Integer.parseInt(st.nextToken());
            if (i-2<0){
                bw.write((a[j-1])+"\n");
            }else {
            bw.write((a[j-1]-a[i-2])+"\n");
            }
        }

        bw.flush();
        bw.close();

    }
}
