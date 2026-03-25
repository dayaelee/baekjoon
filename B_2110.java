import java.io.*;
import java.util.*;

public class Main {
    public static void main(String[] args) throws IOException {
        // 이 부분을 추가하면 콘솔 입력 대신 input.txt 파일을 읽습니다.
        // 제출할 때는 이 줄만 주석 처리하거나 지우면 됩니다!
        // System.setIn(new FileInputStream("input.txt"));
        BufferedReader  br = new BufferedReader(new InputStreamReader(System.in));



        String str = br.readLine();
        StringTokenizer st = new StringTokenizer(str);

        int n,  c; 
        n = Integer.parseInt(st.nextToken());
        c = Integer.parseInt(st.nextToken());

        long[] arr = new long[n];
        
        for(int i = 0; i<n; i++){
            arr[i]=Long.parseLong(br.readLine());
        }

        long l = 1;
        long r = arr[n-1];
        long ans = -1;
        
        Arrays.sort(arr);
        
        while(l<=r){
            long now = (l+r)/2; // 길이 
            // System.out.println("l: "+l+ " r:"+r);
            
            // int dis=1; // 최대거리 
            int cnt = 1; // 공유기 설치 대수
            long d = arr[0];

            for(int i = 1; i<n; i++){
                if(arr[i]-d>=now){ 
                    cnt+=1;
                    d=arr[i];
                }
            }

            // System.out.println("cnt: "+cnt+ " now:"+now);
            
            if(cnt>=c){
                ans = now;
                l=now+1;
            }else{
                r=now-1;
            }
        }

        
        System.out.println(ans);

    }
    
}
