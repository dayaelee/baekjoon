import java.io.*;
import java.util.*;
public class Main {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));

        String str = br.readLine();

        int n = Integer.parseInt(str);

        str = br.readLine();
        String[] numbers = str.split(" ");
        int[] intArr = Arrays.stream(numbers).mapToInt(Integer::parseInt).toArray();

        Arrays.sort(intArr);

        int[] checkIndexs;
        if(intArr.length%2==0){
            checkIndexs = new int[2];
            checkIndexs[0] = intArr.length/2;
            checkIndexs[1] = checkIndexs[0]-1;
        }else{
            checkIndexs = new int[1];
            checkIndexs[0] = intArr.length/2;

        }

        int minV=Integer.MAX_VALUE;
        int remEle=200000;
        for(int i = 0; i<checkIndexs.length; i++){
            int sum = 0;
            int idx = checkIndexs[i];
            for(int j = 0; j<n; j++){
                if(intArr[idx]==intArr[j]){
                    continue;
                }else{
                    if (intArr[idx]>intArr[j]){
                        sum += intArr[idx] - intArr[j];
                    }else if (intArr[idx]<intArr[j]){
                        sum += intArr[j] - intArr[idx];
                    }
                }
            }
            if(minV >= sum){
                if(remEle>intArr[idx]){
                    remEle = intArr[idx];
                }
            }
        }
        System.out.println(remEle);
    }
}
