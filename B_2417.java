import java.io.*;
import java.util.*;
public class Main {

    static long calcInterSqrt(long x){
        if (x == 0) return 0;

        long l = 1, r = 1L<<32, sqrt = -1;
        while(l<=r){
            long m = (r+l)/2;
            if(isIntegerSqrt(x, m)){
                r=m-1;
                sqrt = m;
            }
            else l = m+1;
        }

        return sqrt;
    }

    static boolean isIntegerSqrt(long n, long q){
        long qq = n/q;

        if(n%q !=0) qq++;
        return q>=qq;
    }


    public static void main(String[] args) throws IOException   {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));
        String str = br.readLine();

        long n = Long.parseLong(str);

        System.out.println(calcInterSqrt(n));



    }
    
}
