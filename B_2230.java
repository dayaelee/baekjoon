import java.io.*;
import java.util.*;
public class Main {
    public static void main(String[] args) throws IOException {
        // 이 부분을 추가하면 콘솔 입력 대신 input.txt 파일을 읽습니다.
        // 제출할 때는 이 줄만 주석 처리하거나 지우면 됩니다!
        // System.setIn(new FileInputStream("input.txt"));

        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));

        String str = br.readLine();

        StringTokenizer st = new StringTokenizer(str);
        int n = Integer.parseInt(st.nextToken());
        int m = Integer.parseInt(st.nextToken());

        int[] arr = new int[n];
        
        for(int i = 0; i<n; i++){
            str = br.readLine();
            arr[i]=Integer.parseInt(str);
        }

        int l=0, r=1, ans = Integer.MAX_VALUE;

        Arrays.sort(arr);

        while(true){
            // System.out.println("l: "+ l+"  r: "+r);
            if(r>=n){
                break;
            }
            if(arr[r]-arr[l]<m){
                r++;
            } else if (r>n){
                if( l<n){
                    l+=1;
                    r=l+1;
                }else{
                    break;
                }
            } else{
                ans=Math.min(arr[r]-arr[l], ans);
                l+=1;
                r=l+1;
            }
        }

        System.out.println(ans);











    }
    
}
