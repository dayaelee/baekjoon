import java.io.*;
import java.util.*;

public class Main {
    public static int N;
    public static int[] arr;
    public static int[] answer;
    public static boolean[] visited;
    public static int maxValue;

    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        String str = br.readLine();

        N = Integer.parseInt(str);

        arr = new int[N];
        answer = new int[N];

        str = br.readLine();
        StringTokenizer st = new StringTokenizer(str);
        maxValue = 0;
        visited = new boolean[10000002];
        
        for(int i = 0; i<N; i++){
            arr[i]=Integer.parseInt(st.nextToken());
            maxValue = Math.max(maxValue, arr[i]);
            int value = arr[i];
            visited[value]=true;
        }
        
        answer = new int[10000002];
        Arrays.fill(answer, 0);

        for(int i = 0; i<N; i++){
            for(int j = 2*arr[i]; j<=maxValue; j+=arr[i]){
                if (visited[j]==true){
                    answer[j]-=1;
                    int origin=arr[i];
                    answer[origin]+=1;  
                }
            }
        }
        StringBuilder sb = new StringBuilder();
        for(int i = 0; i<N; i++){
            int index = arr[i];
            
            sb.append(answer[index]+" ");
        }
        System.out.println(sb.toString());
    }
}
