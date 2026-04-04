import java.io.*;
import java.util.*;

public class Main {
    public static void main(String[] args) throws IOException {
        // 이 부분을 추가하면 콘솔 입력 대신 input.txt 파일을 읽습니다.
        // 제출할 때는 이 줄만 주석 처리하거나 지우면 됩니다!
        System.setIn(new FileInputStream("input.txt"));

        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        int n = Integer.parseInt(br.readLine());

        while(n-->0){
            Deque<Integer> d = new ArrayDeque<>();
            String str = br.readLine();
            int endFlag=0;
            for(int i=0; i<str.length(); i++){
                char c = str.charAt(i);
                if(c=='('){
                    d.addLast(1);
                }else{
                    if (d.isEmpty()) {
                        System.out.println("NO");
                        endFlag=1;
                        break;
                    }
                    else d.pollLast();
                }
            }
            if(endFlag==0){
                if(d.size()==0) System.out.println("YES");
                else System.out.println("NO");
            }
        }
    }
    
}