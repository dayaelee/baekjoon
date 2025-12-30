import java.io.*;
import java.util.*;
public class Main {
    public static int check;
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        String str = br.readLine();

        ArrayList<Character> ans = new ArrayList<>();
        ArrayList<Character> basket = new ArrayList<>();
        check = 0;
        StringBuilder sb = new StringBuilder();
        for(int i = 0; i<str.length(); i++){
            if(str.charAt(i)=='<'){
                check = 1;

                if (!basket.isEmpty()){
                    List<Character> tmp = new ArrayList<>(basket);
                    Collections.reverse(tmp);
                    for(char c : tmp){
                        sb.append(c);
                    }
                    basket.clear();
                }
                sb.append(str.charAt(i));
            }else if (str.charAt(i)=='>'){
                check = 0;
                sb.append(str.charAt(i));
            }else{
                if(check==0){
                    if(str.charAt(i)!=' '){
                        basket.add(str.charAt(i));
                    }else{
                        if (!basket.isEmpty()){
                            List<Character> tmp = new ArrayList<>(basket);
                            Collections.reverse(tmp);
                            for(char c : tmp){
                                sb.append(c);
                            }
                            sb.append(' ');
                            basket.clear();
                        }else{
                            sb.append(' ');
                        }
                    }
                }else if(check==1){
                    sb.append(str.charAt(i));
                }
            }
            
        }
        if (!basket.isEmpty()){
            List<Character> tmp = new ArrayList<>(basket);
            Collections.reverse(tmp);
            for(char c : tmp){
                sb.append(c);
            }
        }
        System.out.println(sb.toString());
    }
    
}
