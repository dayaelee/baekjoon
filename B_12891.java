import java.io.*;
import java.util.*;

public class Main {
    public static int s, p;
    public static String tmp;
    public static int[] check;
    public static int answer;
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        String str = br.readLine();
        StringTokenizer st = new StringTokenizer(str);

        s = Integer.parseInt(st.nextToken());
        p = Integer.parseInt(st.nextToken());

        tmp = br.readLine();

        check = new int[4];
        str = br.readLine();
        st = new StringTokenizer(str);
        for(int i = 0; i<4; i++){
            check[i]=Integer.parseInt(st.nextToken());
        }
        
        answer = 0;
        int start = 0;
        int end = p-1;
        int[] copppy = check.clone();
        for(int i = start; i <= end; i++){
            char target = tmp.charAt(i);
            if (target=='A'){
                copppy[0]-=1;
            }else if(target=='C'){
                copppy[1]-=1;
            }else if(target=='G'){
                copppy[2]-=1;
            }else if(target=='T'){
                copppy[3]-=1;
            }
        }

        while(true){
            if(copppy[0]<=0 && copppy[1]<=0 && copppy[2]<=0 && copppy[3]<=0){
                answer+=1;
            }

            end+=1;
            if (end>=s){
                break;
            }

            // 복구 
            char target = tmp.charAt(start);
            if (target=='A'){
                copppy[0]+=1;
            }else if(target=='C'){
                copppy[1]+=1;
            }else if(target=='G'){
                copppy[2]+=1;
            }else if(target=='T'){
                copppy[3]+=1;
            }
            // 뒤로간다 
            target = tmp.charAt(end);
            if (target=='A'){
                copppy[0]-=1;
            }else if(target=='C'){
                copppy[1]-=1;
            }else if(target=='G'){
                copppy[2]-=1;
            }else if(target=='T'){
                copppy[3]-=1;
            }
            start+=1;
        }

        System.out.println(answer);
    }
    
}