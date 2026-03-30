import java.util.*;
import java.io.*;


public class Main {
    public static void main(String[] args) throws IOException {

        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        String str = br.readLine();
        int n = Integer.parseInt(str);
        str = br.readLine();

        Map<Character, Integer> s = new HashMap<Character, Integer>();

        int l=0, r=0, cnt=1, ans=1;

        s.put(str.charAt(l), 1);

        while(l<str.length() && r<str.length()){

            // System.out.println(s.toString()+" l: "+l +" r: "+r+ " cnt: "+cnt);
            r+=1;
            if (r==str.length()){
                break;
            }

            char nc = str.charAt(r);
            if(s.containsKey(nc)){
                cnt+=1;
                s.put(nc, s.get(nc)+1);
            }else{
                if(s.size()<n){
                    s.put(nc, 1);
                    cnt+=1;
                }else{
                    char target = str.charAt(l);
                    int counts = s.get(target);
                    l++;
                    cnt -= 1;
                    if (counts>1){
                        s.put(target, counts-1);
                        r--;
                    }else{
                        s.remove(target);
                        s.put(nc, 1);
                        cnt+=1;
                    }
                }
            }
            ans=Math.max(cnt, ans);
        }

        System.out.println(ans);
    }
}
