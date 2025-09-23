import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.sql.SQLOutput;
import java.util.*;

public class Main {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        String str = br.readLine();

        StringTokenizer st = new StringTokenizer(str);

        int a = Integer.parseInt(st.nextToken());
        int b = Integer.parseInt(st.nextToken());

        str = br.readLine();
        st = new StringTokenizer(str);

        int c = Integer.parseInt(st.nextToken());
        int d = Integer.parseInt(st.nextToken());

        if (a+c<b+d){
            System.out.println("Hanyang Univ.");
        } else if (a+c>b+d) {
            System.out.println("Yongdap");

        }else {
            System.out.println("Either");
        }


    }
}

