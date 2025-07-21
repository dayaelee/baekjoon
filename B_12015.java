import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.ArrayList;
import java.util.StringTokenizer;

public class Main {
    public static int[] arr;
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        String str = br.readLine();
        int n = Integer.parseInt(str);
        str = br.readLine();
        StringTokenizer st = new StringTokenizer(str);
        arr = new int[n];

        for (int i = 0; i < n; i++) {
            arr[i]=Integer.parseInt(st.nextToken());
        }

        ArrayList<Integer> lis = new ArrayList<>();
        lis.add(0);
        int cnt=0;
        for (int i = 0; i < n; i++) {
            if (lis.get(cnt) < arr[i]){
                cnt+=1;
                lis.add(arr[i]);

            }
            else if (lis.get(cnt)>arr[i]){
                int idx = bSearch(lis, arr[i]);
                lis.set(idx, arr[i]);
            }
        }
        System.out.println(lis.size()-1);
    }

    public static int bSearch(ArrayList<Integer> lis, int target){
        int start=0, end=lis.size();
        while (start <=end){
            int mid = (start+end)/2;
            if (lis.get(mid) < target){
                start = mid +1;
            }else {
                end = mid - 1;
            }
        }
        return start;
    }
}