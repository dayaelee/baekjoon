import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.StringTokenizer;

public class Main {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        String str = br.readLine();

        int p = Integer.parseInt(str);

        for (int i = 0; i < p; i++) {
            str = br.readLine();
            StringTokenizer st = new StringTokenizer(str);
            int[] students = new int[21];
            int cnt = 0;
            int answer = 0;
            int t = -1;
            for (int j = 0; j < 21; j++) {
                int inputValue = (Integer.parseInt(st.nextToken()));
                if (j == 0){
                    t = inputValue;
                }
                if (j==1) {
                    students[0] = inputValue;
                    cnt +=1;
                } else if (j>1) {
                    for (int k = 0; k < cnt; k++) {
                        if (students[k]<inputValue) {
                            if (k==cnt-1){
                                students[cnt]=inputValue;
                                cnt+=1;
                                break;
                            }
                        }else{
                            if(k<cnt){
                                int nowStart = k;
                                int nowEnd = cnt-1;
                                for (int l = nowEnd; l >= nowStart ; l--) {
                                    students[l+1]=students[l];
                                    answer+=1;
                                }
                                students[nowStart]=inputValue;
                                cnt+=1;
                                break;
                            }
                        }
                    }
                }
            }
            System.out.println((t)+" "+answer);
        }
    }
}

