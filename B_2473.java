import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.Arrays;
import java.util.StringTokenizer;

import static java.lang.Math.abs;

public class Main {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        int n = Integer.parseInt(br.readLine());

        String str = br.readLine();
        StringTokenizer st = new StringTokenizer(str);

        int[] arr = new int[n];
        for (int i = 0; i < n; i++) {
            arr[i]=Integer.parseInt(st.nextToken());
        }

        Arrays.sort(arr);

        long resultSum=3000000000L;
        int[] result=new int[3];

        for (int i = 0; i < n-2; i++) {
            int left = i+1;
            int right = n-1;
            while(left<right){
                long sum = (long)arr[i]+arr[left]+arr[right];

                if (resultSum>abs(sum)){
                    resultSum=abs(sum);
                    result[0]=arr[i];
                    result[1]=arr[left];
                    result[2]=arr[right];
                }

                if (sum > 0){
                    right-=1;
                } else if (sum<0){
                    left+=1;
                } else{
                    System.out.println(result[0] + " "+result[1] +" "+ result[2]);
                    return;
                }
            }
        }
        System.out.println(result[0] + " "+result[1] +" "+ result[2]);
    }
}