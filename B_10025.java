import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.Arrays;
import java.util.StringTokenizer;

public class Main {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        String str = br.readLine();
        StringTokenizer st = new StringTokenizer(str);
        int n, k;
        n = Integer.parseInt(st.nextToken());
        k = Integer.parseInt(st.nextToken());
        int[] arr = new int[1000001];
        int start = 1000000;
        int end = 0;
        for (int i = 0; i < n; i++) {
            str = br.readLine();
            st = new StringTokenizer(str);
            int value = Integer.parseInt(st.nextToken());
            int index = Integer.parseInt(st.nextToken());
            arr[index]=value;
            if (index<start){
                start = index;
            }

            if (index> end){
                end = index;
            }
        }

        int answer = 0;
        int tmpSum = 0;
        int first = 1;
        while (start<=1000000){
            int tmpEnd = Math.min(1000000, start+(2*k));
//            System.out.println("start: "+start+" tmpEnd: "+tmpEnd);
            if (first==1){
                for (int i = start; i <= tmpEnd; i++) {
                    tmpSum+=arr[i];
                }
                first=0;
            }else{
                tmpSum+=arr[tmpEnd];
            }
            if (tmpSum>answer){
                answer=tmpSum;
            }
            tmpSum-=arr[start];
            start+=1;

        }

        System.out.println(answer);

    }
}