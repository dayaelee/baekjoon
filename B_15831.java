import java.util.*;
import java.io.*;


public class Main {
    public static void main(String[] args) throws IOException {

        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        String str = br.readLine();
        StringTokenizer st = new StringTokenizer(str);
        int n = Integer.parseInt(st.nextToken());
        int b = Integer.parseInt(st.nextToken());
        int w = Integer.parseInt(st.nextToken());

        str = br.readLine();
        int l=0, r=0, nb=0, nw=0, ans = 0;

        // 초기화 
        if(str.charAt(l)=='B'){
            nb+=1;
        }else{
            nw+=1;
        }

        while(l<n && r<n){
            if(nb<=b && nw>=w){
                ans=Math.max(ans, r+1-l);
            }

            r+=1;
            if(r==n){
                break;
            }

            if(str.charAt(r)=='B'){
                nb+=1;
            }else{
                nw+=1;
            }

            if(nb>b){
                if(str.charAt(l)=='W'){
                    nw-=1;
                }else{
                    nb-=1;
                }
                l+=1;
            }
        }
        System.out.println(ans);
    }
}
