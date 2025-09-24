import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.sql.SQLOutput;
import java.util.*;

public class Main {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        String str = br.readLine();



        int a = Integer.parseInt(str);
        if (a>0)
            a = a*3;

        str = br.readLine();
        int c = Integer.parseInt(str);
        if (c>0)
            c = c*4;

        str = br.readLine();
        int d = Integer.parseInt(str);
        if (d>0)
            d = d*5;


        System.out.println(a+c+d);


    }
}

