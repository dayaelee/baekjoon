import java.io.*;
import java.util.*;

public class Main {
    public static void main(String[] args) throws IOException {
        // 이 부분을 추가하면 콘솔 입력 대신 input.txt 파일을 읽습니다.
        // 제출할 때는 이 줄만 주석 처리하거나 지우면 됩니다!
        System.setIn(new FileInputStream("input.txt"));

        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        
        String str = br.readLine();

        int openCnt = 0;
        int ans =0;
        for(int i = 0; i<str.length(); i++){
            if(str.charAt(i)=='(') openCnt++;
            else {// )
                openCnt--;
                if (str.charAt(i-1) =='(')// 레이저면 
                    ans+=openCnt;
                else ans++;
            }
        }
        System.out.println(ans);
    }
    
}
