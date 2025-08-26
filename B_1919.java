import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.ArrayList;
import java.util.HashMap;
import java.util.List;

public class Main {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        String str = br.readLine();
        String str2 = br.readLine();

        char [] arr = str.toCharArray();
        List<Integer> list = new ArrayList<>();
        List<Integer> list2 = new ArrayList<>();
        int answer =0;
        int n = str.length();
        List<Character> c = new ArrayList<>();


        for (int i = 0; i < n; i++) {
            for (int j = 0; j < str2.length(); j++) {
                if (str.charAt(i) != str2.charAt(j)){
                    continue;
                }else{
                    if (!list.contains(j)) {
                        list.add(j);
//                        char tmp = str2.charAt(j);
//                        c.add(tmp);
                        break;
                    }
                }
            }
        }

        for (int i = 0; i < str2.length(); i++) {
            for (int j = 0; j < n; j++) {
                if (str2.charAt(i) != str.charAt(j)){
                    continue;
                }else{
                    if (!list2.contains(j)) {
                        list2.add(j);
//                        char tmp = str2.charAt(j);
//                        c.add(tmp);
                        break;
                    }
                }
            }
        }


//        System.out.println(list.toString());
//        System.out.println(list2.toString());
        for (int i = 0; i < n; i++) {
            if (!list2.contains(i)){
                answer+=1;
            }

        }

        for (int i = 0; i < str2.length(); i++) {
            if (!list.contains(i)){
                answer+=1;
            }

        }
        System.out.println(answer);
    }
}
