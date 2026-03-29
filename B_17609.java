import java.util.*;
import java.io.*;


public class Main {
    public static void main(String[] args) throws IOException {
        // 이 부분을 추가하면 콘솔 입력 대신 input.txt 파일을 읽습니다.
        // 제출할 때는 이 줄만 주석 처리하거나 지우면 됩니다!
        System.setIn(new FileInputStream("input.txt"));

        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));

        String str = br.readLine();
        int n = Integer.parseInt(str);

        for(int i = 0; i<n; i++){
            String s =br.readLine();

            int cnt = 0, l = 0, r = s.length()-1;
            
            while(l<r){
                // System.out.println("l: "+l + "r: "+r+" cnt:"+cnt);
                if (s.charAt(l)== s.charAt(r)){
                    l++;
                    r--;
                } else{
                    if(s.charAt(l+1)==s.charAt(r)){
                        l++;
                        cnt+=1;
                    }else if (s.charAt(l)==s.charAt(r-1)){
                        r--;
                        cnt+=1;
                    }else{
                        l++;
                        // r--;
                        cnt+=1;
                    }
                }
            }

            int cnt2=0;
            l = 0;
            r = s.length()-1;
            while(l<r){
                // System.out.println("l: "+l + "r: "+r+" cnt2:"+cnt2);
                if (s.charAt(l)== s.charAt(r)){
                    l++;
                    r--;
                } else{
                    if (s.charAt(l)==s.charAt(r-1)){
                        r--;
                        cnt2+=1;
                    } else if(s.charAt(l+1)==s.charAt(r)){
                        l++;
                        cnt2+=1;
                    } else{
                        l++;
                        cnt2+=1;
                    }
                }
            }
            int ans = Math.min(cnt, cnt2);
            
            System.out.println(Math.min(cnt, cnt2)>=2? 2: ans);
            
        }

        
    }
    
}
