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

        int size = Integer.parseInt(str);

        Queue<Integer> q  = new LinkedList<>();
        while(true){
            int v = Integer.parseInt(br.readLine());
            if(v>=1){
                if(q.size()==size) continue;
                else q.offer(v);
            } else if (v ==0){
                if(q.size()>=1) q.poll();
            } else if (v == -1){
                break;
            }
        }

        if(q.size()==0){
            bw.write("empty");
        }else{
            while(!q.isEmpty()){
                bw.write(q.poll()+" ");
            }
            bw.flush();
        }
        bw.close();
    }
}
