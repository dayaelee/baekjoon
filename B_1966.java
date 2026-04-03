import java.io.*;
import java.util.*;


public class Main {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        String str = br.readLine();

        int t = Integer.parseInt(str);
        for(int i = 0; i<t; i++){
            str = br.readLine();
            StringTokenizer st = new StringTokenizer(str);
            int n = Integer.parseInt(st.nextToken());
            int m = Integer.parseInt(st.nextToken());

            str = br.readLine();
            Queue<Integer> q = new LinkedList<>();
            Queue<Integer> q2 = new LinkedList<>();
            HashMap<Integer, Integer> hm = new HashMap<>();
            st = new StringTokenizer(str);
            for(int j = 0; j<n; j++){
                int v = Integer.parseInt(st.nextToken());
                q.offer(v);
                q2.offer(j);
                if(hm.containsKey(v)){
                    hm.put(v, hm.get(v)+1);
                } else {
                    hm.put(v, 1);
                }
            }

            int mp = 9;

            int cnt = 0;
            int end=0;
            while(!q.isEmpty()){
                int repeat = 0;
                if(hm.containsKey(mp)){
                    repeat = hm.get(mp);
                }else{
                    mp--;
                    continue;
                }
                while(true){
                    if(q.peek()==mp){
                        q.poll();
                        int check = q2.poll();
                        cnt++;
                        repeat--;
                        if (check ==m){
                            System.out.println(cnt);
                            end=1;
                            break;
                        }
                    }else{
                        int vv = q.poll();
                        int vv2 = q2.poll();
                        q.offer(vv);
                        q2.offer(vv2);
                    }
                    if (repeat==0){
                        mp--;
                        break;
                    }
                }

                if (end==1){
                    break;
                }

            }
        }
    }
}
