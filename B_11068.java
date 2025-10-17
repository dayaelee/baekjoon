import java.io.*;
import java.util.*;

public class B_11068 {
    public static void main(String[] var0) throws IOException{
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));

        String str = br.readLine();

        int t = Integer.parseInt(str);
        while(t-- >0){
            str = br.readLine();

            
            int origin = Integer.parseInt(str);
            boolean tflag = false;
            for (int j =2; j<= 64; j++){
                    
                //String target = Integer.toString(tmp, j);
                // 진법 변환
                int tmp = origin;

                String answer = "";
                while (tmp>0) {
                    int d = tmp%j;
                    
                    if (d<10){
                        answer+=d;
                    }else{
                        answer+= (char)((d-10)+'A');
                    }
                    tmp = tmp/j;
                    
                }

                // System.out.println("hi: "+ answer);

                StringBuilder ans = new StringBuilder();
                ans.append(answer);
                ans.reverse();

                String target = ans.toString();

                // System.out.println("^^target: j: "+j+" "+ target);
                StringBuilder sbL = new StringBuilder();
                StringBuilder sbR = new StringBuilder();
                
                
                if (target.length()%2==0){
                    sbL.append(target.substring(0, target.length()/2));
                    sbR.append(target.substring(target.length()/2));
                    sbR.reverse();
                    // System.out.println("^^sbL: "+sbL+" sbR: "+ sbR);
                    if (sbL.toString().equals(sbR.toString())){
                        tflag = true;
                        break;
                    }
                }else{
                    sbL.append(target.substring(0, (target.length()/2)));
                    sbR.append(target.substring((target.length()/2)+1));
                    sbR.reverse();
                    // System.out.println("^^sbL: "+sbL+" sbR: "+ sbR);
                    if (sbL.toString().equals(sbR.toString())){
                        tflag = true;
                        break;
                    }
                }
            }
            if (tflag==true){
                bw.write(1+"\n");
            }else{
                bw.write(0+"\n");
            }
        }


        bw.flush();
        bw.close();
    }
}
