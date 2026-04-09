import java.io.*;
import java.util.*;


public class Main {
    public static void main(String[] args) throws IOException {
        // 이 부분을 추가하면 콘솔 입력 대신 input.txt 파일을 읽습니다.
        // 제출할 때는 이 줄만 주석 처리하거나 지우면 됩니다!
        System.setIn(new FileInputStream("input.txt"));

        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        
        int n = Integer.parseInt(br.readLine());

        String[] tmp = br.readLine().split(" ");


        int now =0;
        for(int i = 0; i<n; i++){
            now+=Integer.parseInt(tmp[i]);
        }

        if(now>=1){
            System.out.println("Right");
        }else if (now<0){
            System.out.println("Left");
        }else{
            System.out.println("Stay");
        }

        
        
        
    }
    
}
