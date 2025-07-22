import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.ArrayList;
import java.util.StringTokenizer;

public class Main {
    public static Long[] arr;

    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        String str = br.readLine();

        int n = Integer.parseInt(str);
        arr = new Long[n];
        str = br.readLine();
        StringTokenizer st = new StringTokenizer(str);

        for (int i = 0; i < n; i++) {
            arr[i] = Long.parseLong(st.nextToken());
        }

        ArrayList<Long> LIS = new ArrayList<>();
        LIS.add(Long.MIN_VALUE);
        int cnt = 0;
        for (int i = 0; i < n; i++) {
            if (LIS.get(cnt)<arr[i]){
                LIS.add(arr[i]);
                cnt+=1;
            }else if (LIS.get(cnt)>arr[i]){
                int idx = bSearch(LIS, arr[i]);
                LIS.set(idx, arr[i]);
            }
        }
        System.out.println(LIS.size()-1);
    }

    public static int bSearch(ArrayList<Long> lis, long target){
        int start = 0, end = lis.size()-1;
        while (start<=end){
            int mid = (start + end) / 2;

            if (lis.get(mid)<target){
                start=mid+1;
            }else{
                end = mid-1;
            }
        }
        return start;
    }
}