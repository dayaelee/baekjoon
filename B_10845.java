import java.io.*;
import java.util.*;


public class Main {
    public static void main(String[] args) throws IOException {
        // 이 부분을 추가하면 콘솔 입력 대신 input.txt 파일을 읽습니다.
        // 제출할 때는 이 줄만 주석 처리하거나 지우면 됩니다!
        System.setIn(new FileInputStream("input.txt"));

        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));
        String str = br.readLine();

        int n = Integer.parseInt(str);
        Queue<Integer> q = new LinkedList<>();

        int lastValue = -1;
        for(int i = 0; i<n; i++){
            String[] cmd = br.readLine().split(" ");
            if(cmd[0].equals("push")){
                lastValue = Integer.parseInt(cmd[1]);
                q.offer(lastValue);
            }
            else if (cmd[0].equals("pop")){
                if(q.isEmpty()) bw.write("-1\n");
                else bw.write(q.poll()+"\n");
            }

            else if (cmd[0].equals("size")){
                bw.write(q.size()+"\n");

            }
            else if (cmd[0].equals("empty")){
                if(q.isEmpty()) bw.write("1\n");
                else bw.write("0\n");
            }
            else if (cmd[0].equals("front")){
                if(q.isEmpty()) bw.write("-1\n");
                else bw.write(q.peek()+"\n");
            }
            else if (cmd[0].equals("back")){
                if(q.isEmpty()) bw.write("-1\n");
                else bw.write(lastValue+"\n");
            }
        }

        bw.flush();
        bw.close();
        
        
    }
    
}
