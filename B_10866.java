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
        Deque<Integer> q = new LinkedList<>();

        int lastValue = -1;
        for(int i = 0; i<n; i++){
            String[] cmd = br.readLine().split(" ");
            if(cmd[0].equals("push_front")){
                lastValue = Integer.parseInt(cmd[1]);
                q.offerFirst(lastValue);
            }
            else if (cmd[0].equals("push_back")){
                lastValue = Integer.parseInt(cmd[1]);
                q.offerLast(lastValue);
            }
            else if (cmd[0].equals("pop_front")){
                if(q.isEmpty()) bw.write("-1\n");
                else bw.write(q.pollFirst()+"\n");
            }
            else if (cmd[0].equals("pop_back")){
                if(q.isEmpty()) bw.write("-1\n");
                else bw.write(q.pollLast()+"\n");
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
                else bw.write(q.getFirst()+"\n");
            }
            else if (cmd[0].equals("back")){
                if(q.isEmpty()) bw.write("-1\n");
                else bw.write(q.getLast()+"\n");
            }
        }
        bw.flush();
        bw.close();
    }
}
