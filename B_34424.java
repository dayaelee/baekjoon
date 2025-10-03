import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.sql.SQLOutput;
import java.util.*;

public class Main {
    public static boolean flag;
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        String str = br.readLine();
        int x = Integer.parseInt(str);

        str = br.readLine();
        int y = Integer.parseInt(str); 

        System.out.println((x-1)*y);


    }
}

