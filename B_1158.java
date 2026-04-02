import java.io.*;
import java.util.*;
public class Main {
    public static void main(String[] args) throws IOException {
        // 이 부분을 추가하면 콘솔 입력 대신 input.txt 파일을 읽습니다.
        // 제출할 때는 이 줄만 주석 처리하거나 지우면 됩니다!
        System.setIn(new FileInputStream("input.txt"));
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));

        String str = br.readLine();

        StringTokenizer st = new StringTokenizer(str);

        int n = Integer.parseInt(st.nextToken());
        int k = Integer.parseInt(st.nextToken());

        ArrayList<Integer> al = new ArrayList<>();
        for(int i = 0; i<n; i++){
            al.add(i+1);
        }

        int index = 0;
        StringBuilder sb = new StringBuilder();
        sb.append("<");
        while(!al.isEmpty()){
            index=(index+(k-1))%al.size();
            if(al.size()>1)
                sb.append(al.get(index)+", ");
            else
                sb.append(al.get(index)+">");
            // System.out.println(al.get(index));
            al.remove(index);
            
        }

        System.out.println(sb);
    }
    
}
 