import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.sql.SQLOutput;
import java.util.*;

public class Main {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        String str = br.readLine();
        int result = Integer.parseInt(str);

        str = br.readLine();
        int a = Integer.parseInt(str);

        str = br.readLine();
        int b = Integer.parseInt(str);

        if(a*b>=result){
            System.out.println("yes");
        }else {
            System.out.println("no");
        }



    }
}

