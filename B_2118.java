import java.io.*;
import java.util.*;

public class Main {

    public static void main(String[] args) throws IOException  {

        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));

        String str = br.readLine();

        int n = Integer.parseInt(str);

        int[] arr = new int[n+1];
        int[] nu = new int[n+1];

        for(int i = 1; i<=n; i++){
            arr[i] = Integer.parseInt(br.readLine());
            if(i>=2){
                nu[i]+=nu[i-1]+arr[i];
            }else{
                nu[i]=arr[i];
            }
        }

        int l=0, r=l+1, dis=0, dis2=0, ans=0;

        while(true){
            if (r>=n){
                if (l<=n){
                    l++;
                    r=l+1;
                    continue;
                }else{
                    break;
                }
            }

            dis=nu[r]-nu[l];
            dis2 = nu[n]-dis;
            
            if(dis<=dis2){
                ans = Math.max(ans, dis);
            }else{
                ans = Math.max(ans, dis2);
            }
            r++;
        }
        System.out.println(ans);
    }
}
    

