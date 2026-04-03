import java.io.*;
import java.util.*;


public class Main {
    public static void main(String[] args) throws IOException {
        // 이 부분을 추가하면 콘솔 입력 대신 input.txt 파일을 읽습니다.
        // 제출할 때는 이 줄만 주석 처리하거나 지우면 됩니다!
        System.setIn(new FileInputStream("input.txt"));

        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));
        // String str = br.readLine();

        int t = Integer.parseInt(br.readLine());
        while(t-->0){
            String cmd = br.readLine();
            int n = Integer.parseInt(br.readLine());
            String str = br.readLine();
            String cleanInput = str.replace("[", "")
                                    .replace("]", "");
            String[] items = cleanInput.split(",");
            // System.out.println(Arrays.toString(items)+"?"+items.length);

            Deque<Integer> d = new LinkedList<>();
            if(items.length>=1){
                for(int i =0; i<items.length; i++){
                    if(items[i]=="") continue;
                    
                    d.offerLast(Integer.parseInt(items[i]));
                }
            }
            
            
            int flag = 0;
            int endFlag = 0;
            for(int i = 0; i<cmd.length(); i++){
                char c = cmd.charAt(i);
                if(c=='R'){
                    if (flag==0) flag=1;
                    else flag = 0;
                } else if (c=='D'){
                    if(flag ==0){
                        if(d.isEmpty()) {
                            bw.write("error\n"); 
                            endFlag = 1;
                            break;
                        } else d.pollFirst();
                    }else{
                        if(d.isEmpty()) {
                            bw.write("error\n"); 
                            endFlag = 1;
                            break;
                        }
                        else d.pollLast();
                    }
                }
            }


            int size = d.size();

            if(endFlag ==0){
                bw.write("[");
                if(flag==1){
                    while(!d.isEmpty()){
                        int c = d.pollLast();
                        // System.out.println(c);
                        bw.write(c+"");
                        if(size>1)
                            bw.write(",");
                        size--;
                    }
                }else{
                    while(!d.isEmpty()){
                        int c = d.pollFirst();
                        // System.out.println(c);
                        bw.write(c+"");
                        if(size>1)
                            bw.write(",");
                        size--;
                    }
                }
                
                bw.write("]\n");
            }
            


        }


        bw.flush();
        bw.close();
    }
}
