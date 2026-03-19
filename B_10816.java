import java.io.*;
import java.util.*;
public class Main {

    // static int binarySearch(int value, int n, int[] arr){
    //     int start = 0;
    //     int end = n-1;
    //     int cnt=0;
        
    //     boolean[] visited = new boolean[n];
    //     while(start<=end){
    //         int mid = (start+end)/2;

    //         if(arr[start]==value&& visited[start]==false){
    //             visited[start]=true;
    //             cnt+=1;
    //         }

    //         if(arr[end]==value&& visited[end]==false){
    //             visited[end]=true;
    //             cnt+=1;
    //         }

    //         if(arr[mid]>value){
    //             end=mid-1;
    //         }else if (arr[mid]<value) {
    //             start=mid+1;
    //         } else if (arr[mid]==value){
    //             if(visited[mid]==false){
    //                 cnt+=1;
    //                 start+=1;
    //                 visited[mid]=true;
    //             }else{
    //                 start+=1;
    //             }

    //         }
    //     }
    //     return cnt;

    // }
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));
        String str = br.readLine();

        int n = Integer.parseInt(str);

        int[] arr = new int[n];
        str = br.readLine();
        StringTokenizer st = new StringTokenizer(str);

        Map<Integer, Integer> map = new HashMap<Integer, Integer>();
        for(int i = 0; i<n; i++){
            arr[i]=Integer.parseInt(st.nextToken());
            map.put(arr[i], map.getOrDefault(arr[i], 0)+1);
        }

        Arrays.sort(arr);
        
        str = br.readLine();
        int m = Integer.parseInt(str);

        str = br.readLine();
        st = new StringTokenizer(str);

        
        
        for(int i = 0; i<m; i++){
            
            int key =Integer.parseInt(st.nextToken());
            bw.write(map.getOrDefault(key, 0)+" ");
        }

        bw.flush();
        bw.close();
    }
    
}
