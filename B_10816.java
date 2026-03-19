import java.io.*;
import java.util.*;
public class Main {

    static int findLowerBoundIndex(int[] arr, int x){
        // x 이상의 값이 처음으로 나타나는 위치
        int lowerBoundIndex = arr.length;
        int l=0, r=arr.length-1;
        while(l<=r){
            int m = (l+r)/2;
            if(arr[m]<x) l=m+1;
            else{
                r=m-1;
                lowerBoundIndex = m;
            }
        }
        return lowerBoundIndex;
    }

    static int findUpperBoundIndex(int[] arr, int x){
        // x 초과의 값이 처음으로 나타나는 위치 
        int upperBoundIdx = arr.length;
        int l=0, r=arr.length-1;
        while(l<=r){
            int m = (l+r)/2;
            if(arr[m]<=x) l=m+1; 
            else{
                r=m-1;
                upperBoundIdx = m;
            }
        }
        return upperBoundIdx;

    }


    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));
        String str = br.readLine();

        int n = Integer.parseInt(str);

        int[] arr = new int[n];
        str = br.readLine();
        StringTokenizer st = new StringTokenizer(str);

        for(int i = 0; i<n; i++){
            arr[i]=Integer.parseInt(st.nextToken());
        }

        Arrays.sort(arr);
        
        str = br.readLine();
        int m = Integer.parseInt(str);

        str = br.readLine();
        st = new StringTokenizer(str);

        for(int i = 0; i<m; i++){
            
            int key =Integer.parseInt(st.nextToken());
            bw.write(findUpperBoundIndex(arr, key)-findLowerBoundIndex(arr, key)+" ");
        }
        bw.write("\n");
        bw.flush();
        bw.close();
    }
    
}
