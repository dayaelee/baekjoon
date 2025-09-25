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

        str = br.readLine();
        int b = Integer.parseInt(str);

        str = br.readLine();
        int c = Integer.parseInt(str);

        ArrayList<Integer> arr = new ArrayList<>();
        arr.add(a);
        arr.add(b);
        arr.add(c);

        int minBurger = Collections.min(arr);

        str = br.readLine();
        int d = Integer.parseInt(str);

        str = br.readLine();
        int e = Integer.parseInt(str);

        ArrayList<Integer> arr2 = new ArrayList<>();
        arr2.add(d);
        arr2.add(e);

        int minDrink = Collections.min(arr2);

        System.out.println(minDrink+minBurger-50);


    }
}

