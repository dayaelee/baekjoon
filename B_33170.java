import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.sql.SQLOutput;
import java.util.*;

public class B_33170 {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        String str = br.readLine();
        int x = Integer.parseInt(str);

        str = br.readLine();
        int y = Integer.parseInt(str);

        str = br.readLine();
        int z = Integer.parseInt(str);

        if (x+y+z<=21)
            System.out.println(1);
        else
            System.out.println(0);

        
    }
}

