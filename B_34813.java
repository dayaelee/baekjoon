import java.io.*;
import java.util.*;


public class Main {
    public static void main(String[] args) throws IOException {
        // 이 부분을 추가하면 콘솔 입력 대신 input.txt 파일을 읽습니다.
        // 제출할 때는 이 줄만 주석 처리하거나 지우면 됩니다!
        System.setIn(new FileInputStream("input.txt"));

        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        
        String tmp = br.readLine();

        char a = tmp.charAt(0);

        if(a=='F'){
            System.out.println("Foundation");
        }
        else if (a=='C'){
            System.out.println("Claves");
        }
        else if (a=='V'){
            System.out.println("Veritas");
        }
        else if (a=='E'){
            System.out.println("Exploration");
        }
        
    }
    
}
