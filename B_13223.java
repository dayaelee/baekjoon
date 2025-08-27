import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;

public class Main {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));

        String nt = br.readLine();
        String tt = br.readLine();

        if (nt.equals(tt)){
            System.out.println("24:00:00");
        }else {
            String[] ntArr = nt.split(":");
            String[] ttArr = tt.split(":");

            int[] answer = {0, 0, 0};


            for (int i = 0; i < 3; i++) {
                int ntt = Integer.parseInt(ntArr[i]);
                int ttt = Integer.parseInt(ttArr[i]);
                if (ntt > ttt) {
                    if (i == 0) {
                        answer[0] = (24 - ntt) + ttt;

                    } else {
                        if (answer[i-1]>0){
                            answer[i - 1] -= 1;
                            answer[i] = (60 - ntt) + ttt;
                        } else{
                            answer[i-2]-=1;
                            answer[i-1]+=60;
                            answer[i - 1] -= 1;
                            answer[i] = (60 - ntt) + ttt;
                        }
                    }
                } else {
                    answer[i] = ttt - ntt;
                }
            }

            for (int i = 0; i < 3; i++) {
                if (i == 0) {
                    if (answer[i] < 10) {
                        System.out.print("0" + answer[i]);
                    } else {
                        System.out.print(answer[i]);
                    }
                } else {
                    if (answer[i] < 10) {
                        System.out.print(":0" + answer[i]);
                    } else {
                        System.out.print(":" + answer[i]);
                    }
                }
            }
        }
    }
}
