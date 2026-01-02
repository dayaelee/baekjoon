import java.util.*;
import java.io.*;

public class Main {
    public static int N;
    public static double[] arr;
    public static String str;
    
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        String s = br.readLine();
        
        N = Integer.parseInt(s);
        str = br.readLine();

        arr = new double[N];
        
        for(int i = 0; i<N; i++){
            s = br.readLine();
            arr[i]=Double.parseDouble(s);
        }

        ArrayDeque<Double> stack1 = new ArrayDeque<>();

        for(int i = 0; i<str.length(); i++){
            char c = str.charAt(i);
            double t;
            if (c>='A' && c<='Z'){
                stack1.push(arr[c-'A']);
            }else{
                Double b = stack1.pop();
                Double a = stack1.pop();    
                
                switch(c){
                    case '+': 
                        t = a+b;
                        stack1.push(t);
                        break;
                    case '-': 
                        t = a-b;
                        stack1.push(t);
                        break;
                    case '/': 
                        t = a/b;
                        stack1.push(t);
                        break;
                    case '*': 
                        t = a*b;
                        stack1.push(t);
                        break;
                }
            }
        }
        System.out.printf("%.2f", stack1.peek());   
    }
}
