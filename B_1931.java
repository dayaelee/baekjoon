import java.util.*;
import java.io.*;


public class Main {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        String tmp = br.readLine();

        int n = Integer.parseInt(tmp);

        int[][] arr = new int[n][2];

        for(int i = 0; i<n; i++){
            tmp = br.readLine();
            StringTokenizer st = new StringTokenizer(tmp);
            int a = Integer.parseInt(st.nextToken());
            int b = Integer.parseInt(st.nextToken());

            arr[i][0]=a;
            arr[i][1]=b;
        }

        Arrays.sort(arr, (a1, a2)-> {
            if (a1[1] == a2[1]){
                return a1[0]-a2[0];
            }
            return a1[1]-a2[1];
        });

        int answer = 0;
        int now = -1;
        for(int i=0; i<n; i++){
            if (i==0){
                answer = 1;
                now = arr[i][1];
            }else{
                if(arr[i][0]>=now){
                    answer+=1;
                    now=arr[i][1];
                }
            }
            // System.out.println(arr[i][0]+" "+arr[i][1]);
        }

        System.out.println(answer);

    }
    
}
