import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.StringTokenizer;

public class Main {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        String str = br.readLine();
        StringTokenizer st = new StringTokenizer(str);
        int w = Integer.parseInt(st.nextToken());
        int h = Integer.parseInt(st.nextToken());
        str= br.readLine();
        st = new StringTokenizer(str);
        int p = Integer.parseInt(st.nextToken());
        int q = Integer.parseInt(st.nextToken());
        str= br.readLine();
        int t = Integer.parseInt(str);

        int tx = t % (2 * w);
        int ty = t % (2 * h);

        int dx = 1, dy = 1;
        int currentX = p, currentY = q;

        while(tx-- > 0){
            if (currentX == w) dx = -1;
            else if (currentX ==0) dx = 1;
            currentX += dx;
        }

        while(ty-- >0){ // ty 가 0일때 끝남
            if (currentY == h) dy = -1;
            else if (currentY == 0) dy = 1;
            currentY += dy;
        }
        System.out.println(currentX + " " + currentY);
    }
}
