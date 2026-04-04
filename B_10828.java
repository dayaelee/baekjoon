import java.io.*;
import java.util.*;

public class Main {
    public static void main(String[] args) throws IOException {
        // 이 부분을 추가하면 콘솔 입력 대신 input.txt 파일을 읽습니다.
        // 제출할 때는 이 줄만 주석 처리하거나 지우면 됩니다!
        System.setIn(new FileInputStream("input.txt"));

        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        int n = Integer.parseInt(br.readLine());

        Deque<Integer> stack = new ArrayDeque<>();
        while(n-->0){
            String[] cmd = br.readLine().split(" ");
            
            if(cmd[0].equals("push")){
                stack.addLast(Integer.parseInt(cmd[1]));
            } 
            else if (cmd[0].equals("pop")){
                if(stack.isEmpty()) System.out.println(-1);
                else System.out.println(stack.pollLast());
            } 
            else if (cmd[0].equals("size")){
                System.out.println(stack.size());
            } 
            else if (cmd[0].equals("empty")){
                if(stack.isEmpty()) System.out.println(1);
                else System.out.println(0);
            } 
            else if (cmd[0].equals("top")){
                if(stack.isEmpty()) System.out.println(-1);
                else System.out.println(stack.peekLast());
            } 

        }

        
        
    }
    
}
