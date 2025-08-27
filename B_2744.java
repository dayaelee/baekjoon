import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.Locale;

public class Main {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));

        String str = br.readLine();
        
        String upStr = str.toUpperCase();
        String downStr = str.toLowerCase();

        String answer ="";
        for (int i = 0; i < str.length(); i++) {
            if (97<=str.charAt(i)){
                answer+=upStr.charAt(i);
            }else{
                answer+=downStr.charAt(i);
            }
        }
        System.out.println(answer);
    }
}
