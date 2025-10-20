import java.io.*;
import java.util.*;

public class Main {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));

        String str = br.readLine();

        int n = Integer.parseInt(str);

        char[][] arr = new char[n][n];

        for (int i = 0; i<n; i++){
            str = br.readLine();
            for (int j = 0; j<n; j++){
                arr[i][j] = str.charAt(j);
            }
        }

        int ans = 0;
         ans = Math.max(check(arr, n), ans);

        // 가로 쿡(조짐)
        for (int i = 0; i<n; i++){
            for (int j = 0; j<n-1; j++){
                if (arr[i][j]!=arr[i][j+1]){
                    // 바꿔본다. 
                    char tmp = arr[i][j];
                    arr[i][j]=arr[i][j+1];
                    arr[i][j+1]=tmp;

                    // 체크해본다. 
                    ans = Math.max(check(arr, n), ans);

                    // 원상복구 한다. 
                    tmp = arr[i][j];
                    arr[i][j]= arr[i][j+1];
                    arr[i][j+1]=tmp;

                    // System.out.println("\n i: "+i+" j: "+j);
                    // System.out.println("ans: "+ ans);
                }   
            }
        }

        // 세로 쿡(조짐)
        for (int i = 0; i<n; i++){
            for (int j = 0; j<n-1; j++){
                if (arr[j][i] != arr[j+1][i]){
                    char tmp = arr[j][i];
                    
                    arr[j][i]=arr[j+1][i];
                    arr[j+1][i]=tmp;

                    ans = Math.max(check(arr, n), ans);

                    tmp = arr[j][i];
                    arr[j][i] = arr[j+1][i];
                    arr[j+1][i]=tmp;
                }
            }
        }

        bw.write(ans+"\n");
        bw.flush();
        bw.close();
    }

    public static int check(char[][] arr, int n){
        int retValue = 0;
        int value = 0; // 연속된 값
        char start = '-';
        // 가로 쿡
        for (int i = 0; i<n ; i++){
            for (int j = 0; j<n; j++){
                if (j == 0){ 
                    start = arr[i][j];
                    value = 1; 
                } else{
                    if (start!=arr[i][j]){
                        retValue = Math.max(value, retValue);
                        start = arr[i][j];
                        value = 1;
                    } else {
                        value +=1;
                    }
                }
            }
            retValue = Math.max(value, retValue);
        }

        for (int i = 0; i < n ; i++){
            for (int j = 0; j < n; j++){
                if (j == 0){
                    start = arr[j][i];
                    value = 1;
                }else{
                    if (start!=arr[j][i]){
                        retValue = Math.max(value, retValue);
                        start = arr[j][i];
                        value = 1;
                    } else {
                        value +=1;
                    }
                }
            }
            retValue = Math.max(value, retValue);
        }
        
        return retValue;
    }
}
