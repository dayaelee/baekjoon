import java.io.*;
public class Main {
    public static void main(String[] args) throws IOException {
        // 이 부분을 추가하면 콘솔 입력 대신 input.txt 파일을 읽습니다.
        // 제출할 때는 이 줄만 주석 처리하거나 지우면 됩니다!
        System.setIn(new FileInputStream("input.txt"));

        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));

        int d = Integer.parseInt(br.readLine());

        int v = d/5;
        int i = d%5;

        String tmp = "";
        while(v-->0){
            tmp+="V";
        }

        while(i-->0){
            tmp+="I";
        }

        System.out.println(tmp);


        
        
    }
    
}
