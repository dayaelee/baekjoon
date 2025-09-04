import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.StringTokenizer;

public class Main {
    public static int remIdx;
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        String str = br.readLine();

        StringTokenizer st = new StringTokenizer(str);
        int n = Integer.parseInt(st.nextToken());
        int k = Integer.parseInt(st.nextToken());
        char[] track = new char[n];

        int point = 0;
        int endFlag = 0;

        for (int i = 0; i < k; i++) {
            str = br.readLine();
            st = new StringTokenizer(str);
            int pass = Integer.parseInt(st.nextToken());
            char c = (st.nextToken()).charAt(0);

            while(pass>0){
                pass-=1;
                point-=1;
                if (point ==-1){
                    point = n-1;
                }
            }
            if (track[point]!=0&&track[point]!=c){
                endFlag=1;
            }else{
                track[point] = c;
            }

            if (i==k-1){
                remIdx=point;
            }
        }

        for (int i = 0; i < n; i++) {
            if (track[i]==0){
                track[i]='?';
            }
        }
        String answer = "";
        if(endFlag==0) {
            int cnt = n;
            while (cnt > 0) {
                String tmp ="" + track[remIdx];
                if (!tmp.equals("?") && answer.contains(tmp)){
                    System.out.println("!");
                    endFlag=1;
                    break;
                }else {
                    answer += track[remIdx];
                    remIdx += 1;
                    if (remIdx == n) {
                        remIdx = 0;
                    }
                    cnt -= 1;
                }
            }
            if (endFlag!=1) {
                System.out.println(answer);
            }
        }else{
            System.out.println('!');
        }
    }
}

