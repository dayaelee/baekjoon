import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.ArrayDeque;
import java.util.Deque;
import java.util.StringTokenizer;

public class B_28078 {

    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        String str = br.readLine();

        int n = Integer.parseInt(str);
        int status = 0, cb = 0, cw = 0;
        Deque<Integer> deque = new ArrayDeque<>();
        for (int i = 0; i < n; i++) {
            str = br.readLine();
            StringTokenizer st = new StringTokenizer(str);

            String order = st.nextToken();
            if (order.equals("push")){
                String target = st.nextToken();
                if (target.equals("b")){
                    deque.addLast(1);
                    cb+=1;
                } else if(target.equals("w")){
                    deque.addLast(-1);
                    cw+=1;
                }
            } else if (order.equals("pop") && !deque.isEmpty()){
                int tmp = deque.remove();
                if (tmp == -1){
                    cw-=1;
                }else{
                    cb-=1;
                }
            } else if (order.equals("rotate")){
                String dir = st.nextToken();
                if (dir.equals("l")){
                    status-=1;
                    if(status==-1){
                        status=3;
                    }
                } else if (dir.equals("r")){
                    status+=1;
                    if(status==4){
                        status=0;
                    }
                }
            } else if (order.equals("count")){
                String target = st.nextToken();
                if (target.equals("b")){
                    System.out.println(cb);
                }else if (target.equals("w")){
                    System.out.println(cw);
                }
            }

            if (status==1 || status == 3) {
                if (cw==0){
                    deque = new ArrayDeque<>();
//                        System.out.println(deque.toString()+"hi");
                    cb=0;
                } else {
                    int cnt = 0;
                    if (status==1 && !deque.isEmpty()){
                        while (true){
                            if (deque.remove()==1){
                                cnt+=1;
                                if (deque.isEmpty()){
                                    cb-=cnt;
                                    break;
                                }
                            }else{
                                deque.addFirst(-1);
                                cb-=cnt;
                                break;
                            }
                        }
                    } else if (status == 3 && !deque.isEmpty()){
                        while (true){
                            if (deque.removeLast()==1){
                                cnt+=1;
                                if (deque.isEmpty()){
                                    cb-=cnt;
                                    break;
                                }
                            }else{
                                deque.addLast(-1);
                                cb-=cnt;
                                break;
                            }
                        }
                    }
                }
            }
//            System.out.println(deque.toString()+ " hi");
        }
    }
}
