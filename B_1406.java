import java.io.*;
import java.util.*;
public class Main {
    public static void main(String[] args) throws IOException {
        // 이 부분을 추가하면 콘솔 입력 대신 input.txt 파일을 읽습니다.
        // 제출할 때는 이 줄만 주석 처리하거나 지우면 됩니다!
        System.setIn(new FileInputStream("input.txt"));
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));

        String str = br.readLine();
        int m = Integer.parseInt(br.readLine());

        int cur = str.length();


        LinkedList<Character> l = new LinkedList<>();

        ListIterator<Character> it = l.listIterator();

        for(int i = 0; i<str.length(); i++){
            it.add(str.charAt(i));
        }


        for(int i = 0; i<m; i++){
            String tmp = br.readLine();
            StringTokenizer st = new StringTokenizer(tmp);
            String o = st.nextToken();
            char oo = o.charAt(0);
            if(oo=='P'){
                String t = st.nextToken();
                it.add(t.charAt(0));
                it.hasNext();
            } else if (oo=='L'){
                if(it.hasPrevious()) it.previous();
            } else if(oo=='D'){
                if(it.hasNext()) it.next();
            } else if (oo=='B'){
                // System.out.println();
                if(it.hasPrevious()==false) {
                    continue;
                }else{
                    it.previous();
                    it.remove();
                }
                    
            }

            // System.out.println(l.toString());

        }

        StringBuilder sb = new StringBuilder();
        for(char ch : l){
            sb.append(ch);
        }

        System.out.println(sb);

    }
    
}
 