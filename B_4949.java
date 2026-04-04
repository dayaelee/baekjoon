import java.io.*;
import java.util.*;

public class Main {
    public static void main(String[] args) throws IOException {
        // 이 부분을 추가하면 콘솔 입력 대신 input.txt 파일을 읽습니다.
        // 제출할 때는 이 줄만 주석 처리하거나 지우면 됩니다!
        System.setIn(new FileInputStream("input.txt"));

        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        

        while(true){
            String s = br.readLine();
            if(s.equals(".")) break;
            int endFlag=0;
            Deque<Integer> dq = new ArrayDeque<>();
            for(int i = 0; i<s.length(); i++){
                char c = s.charAt(i);
                if(c=='(') dq.offerLast(1);
                if(c=='[') dq.offerLast(2);

                if(c==')') {
                    if(dq.isEmpty()){
                        System.out.println("no");
                        endFlag=1;
                        break;
                    }
                    else{
                        if(dq.peekLast()==1){
                            dq.pollLast();
                        } else{
                            System.out.println("no");
                            endFlag=1;
                            break;
                        }
                    }
                }
                if(c==']') {
                    if(dq.isEmpty()) {
                        System.out.println("no");
                        endFlag=1;
                        break;
                    }else{
                        if(dq.peekLast()==2){
                            dq.pollLast();
                        } else{
                            System.out.println("no");
                            endFlag=1;
                            break;
                        }
                    }
                }

                


            }
            if(endFlag==0){
                if(dq.size()==0){
                    System.out.println("yes");
                }else{
                    System.out.println("no");
                }
            }
        }
    }
    
}
