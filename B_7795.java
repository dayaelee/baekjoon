public import java.util.*;
import java.io.*;
public class Main {
    public static int t;
    public static int a, b;
    public static Integer[] aArr, bArr;
    public static void main(String[] args) throws IOException  {
        BufferedReader br = new BufferedReader(new InputStreamReader((System.in)));
        String str = br.readLine();

        t = Integer.parseInt(str);
        for(int i = 0; i<t; i++){
            str = br.readLine();
            StringTokenizer st = new StringTokenizer(str);

            a = Integer.parseInt(st.nextToken());
            b = Integer.parseInt(st.nextToken());

            aArr = new Integer[a];
            bArr = new Integer[b];

            int cnt = 0;
            str = br.readLine();
            st = new StringTokenizer(str);
            for(int j = 0; j<a; j++){
                aArr[j]=Integer.parseInt(st.nextToken());
            }
            str = br.readLine();
            st = new StringTokenizer(str);
            for(int j = 0; j<b; j++){
                bArr[j]=Integer.parseInt(st.nextToken());
            }

            Arrays.sort(bArr);
            Arrays.sort(aArr, Collections.reverseOrder());

            int bIndex = 0;
            for (int k = 0; k<a; k++){
                bIndex=0;
                while(bIndex<b){
                    int valueA = aArr[k];
                    int valueB = bArr[bIndex];

                    // System.out.println(valueA+" "+valueB);

                    if(valueA>valueB){
                        cnt+=1;
                        bIndex+=1;
                    }else{
                        bIndex=0;
                        break;
                    }
                }
                
                // System.out.println("k "+cnt);
            }

            System.out.println(cnt);

        }

    }
    
}
 {
    
}
