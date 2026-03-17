import java.util.*;
import java.io.*;

public class Main {
    static class Guitar implements Comparable<Guitar>{
        String s;
        int sum;
        int length;

        Guitar(String s, int sum, int length){
            this.s = s;
            this.sum = sum;
            this.length = length;
        }

        @Override
        public int compareTo(Guitar o){
            if (length == o.length){
                if(sum == o.sum){
                    return s.compareTo(o.s);
                }
                return sum - o.sum;
            } return length - o.length;
        }

    }
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        String str = br.readLine();

        int n = Integer.parseInt(str);

        Guitar[] guitars = new Guitar[n];


        for(int i = 0; i<n; i++){
            str = br.readLine();
            int l = str.length();
            int sum = 0;
            for(int j = 0; j<l; j++){
                if(str.charAt(j)<65){
                    sum+=Character.getNumericValue(str.charAt(j));
                }
            }

            guitars[i]= new Guitar(str, sum, l);
        }

        Arrays.sort(guitars);

        for(int i =0; i<n; i++){
            System.out.println(guitars[i].s);
        }
    }
    
}
