import java.util.*;
import java.io.*;


public class Main {
    public static void main(String[] args) throws IOException {
        // 이 부분을 추가하면 콘솔 입력 대신 input.txt 파일을 읽습니다.
        // 제출할 때는 이 줄만 주석 처리하거나 지우면 됩니다!
        System.setIn(new FileInputStream("input.txt"));

        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));


        String str = br.readLine();
        StringTokenizer st = new StringTokenizer(str);

        int n = Integer.parseInt(st.nextToken());
        int m = Integer.parseInt(st.nextToken());

        int[] a= new int[n];
        int[] b= new int[m];


        str = br.readLine();
        st = new StringTokenizer(str);
        for(int i = 0; i<n; i++ ){
            a[i]=Integer.parseInt(st.nextToken());
        }


        str = br.readLine();
        st = new StringTokenizer(str);
        for(int i = 0; i<m; i++ ){
            b[i]=Integer.parseInt(st.nextToken());
        }

        Arrays.sort(a);
        Arrays.sort(b);

        StringBuilder sb = new StringBuilder();

        int o1=0, o2=0, flag1=0, flag2=0;
        while(o1<=n && o2<=m){

            if(flag1==0 && flag2==1){
                for(int i = o1; i<n; i++){
                    sb.append(a[i]+" ");
                }
                o1=n;
                flag1=1;
            } else if (flag1==1 && flag2==0){
                for(int i = o2; i<m; i++){
                    sb.append(b[i]+" ");
                }
                o2=m;
                flag2=1;
            }   

            if(flag1==1 && flag2==1){
                System.out.println(sb.toString());
                break;
            }

            if(flag1==0 && flag2==0){
                if(a[o1]<b[o2]){
                    sb.append(a[o1]+" ");
                    o1+=1;
                }else if (a[o1]==b[o2]){
                    sb.append(a[o1]+" ");
                    o1+=1;
                    sb.append(b[o2]+" ");
                    o2+=1;
                } else{
                    sb.append(b[o2]+" ");
                    o2+=1;
                }
            }

            
            if(o1==n){
                flag1=1;
            }

            if(o2==m){
                flag2=1;
            }

            // System.out.println(sb.toString()+ flag1+" "+flag2);

        }

        
    }
    
}
