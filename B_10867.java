import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.*;

public class B_10867{
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        String str = br.readLine();

        int n = Integer.parseInt(str);
        Set<Integer> tmps = new HashSet<>();


        str = br.readLine();
        StringTokenizer st = new StringTokenizer(str);
        for (int i = 0; i < n; i++) {
            int ele = Integer.parseInt(st.nextToken());
            tmps.add(ele);
        }

        List<Integer> tmpSet = new ArrayList<>(tmps);
        Collections.sort(tmpSet);

        for (int ele: tmpSet) {
            System.out.print(ele+" ");
        }

    }

}
