import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.*;

public class B_2822 {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));


        Integer [] arr = new Integer[8];
        for (int i = 0; i < 8; i++) {
            String str = br.readLine();
            arr[i]=Integer.parseInt(str);
        }

        Integer [] newArr = arr.clone();

        Arrays.sort(arr, Comparator.reverseOrder());

        int answer =0;
        ArrayList<Integer> a = new ArrayList<>();
        ArrayList<Integer> b = new ArrayList<>();
        for (int i = 0; i < 5; i++) {
            a.add(arr[i]);
            answer += arr[i];
        }


        for (int j = 0; j < 5; j++) {
            for (int i = 0; i < 8; i++) {
                if (newArr[i] == a.get(j)){
                    b.add(i+1);
                }
            }
        }
        System.out.println(answer);
        Collections.sort(b);
        for (int i = 0; i < b.size(); i++) {
            System.out.print(b.get(i)+" ");
        }

    }

}
