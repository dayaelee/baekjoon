import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
public class Main {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        String str = br.readLine();
        String find = br.readLine();
        int beginIdx = 0;
        int endIdx = beginIdx+find.length();
        int answer = 0;
        while(true) {
            if (beginIdx > str.length() || endIdx> str.length()){
                break;
            }
            if (find.equals(str.substring(beginIdx, endIdx))){
                answer+=1;
                beginIdx=endIdx;
                endIdx = beginIdx+find.length();
            } else{
                beginIdx+=1;
                endIdx=beginIdx+find.length();
            }
        }
        System.out.println(answer);
    }
}
