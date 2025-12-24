import java.util.*;
import java.io.*;

public class Main {

    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        
        while(true){
            String str = br.readLine();

            if (str.equals("end")){
                break;
            }else if (str.equals("animal")){
                System.out.println("Panthera tigris");
            }else if (str.equals("tree")){
                System.out.println("Pinus densiflora");
            }else if (str.equals("flower")){
                System.out.println("Forsythia koreana");
            }

        }
    }
}
