import java.io.*;
import java.util.*;

public class Main {
    public static int answer = 0;
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));

        String str = br.readLine();
        Integer N = Integer.parseInt(str);

        int left = 0;
        int right = 1;

        int[] tmp = new int[N];

        for (int i = 0; i<N; i++){
            tmp[i]=i+1;
        }

        int sum = 0;
        sum += tmp[left];
        while (left<=N && right<=N){
            if (right<N){
                sum+=tmp[right];
            }
            

            if (sum<N){
                right+=1;
            }else if(sum==N){
                // System.out.println(left);
                left+=1;
                right+=1;
                answer+=1;
            }else{
                left+=1;
                right = left + 1;
                sum=tmp[left];
            }
        }
        // System.out.println(answer);
        bw.write(answer);
        bw.flush();
        bw.close();
    }
}
