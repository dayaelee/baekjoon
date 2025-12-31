import java.io.*;
import java.util.*;

public class Main {
    public static int check;
    public static int stackOn;
    public static ArrayList<Character> bucket;
    public static ArrayList<Character> ans;
    public static ArrayList<Character> realAns;
    public static ArrayDeque<Character> leftBucket;
    public static void main(String[] args) throws IOException  {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        String str = br.readLine();

        ans = new ArrayList<>();
        bucket = new ArrayList<>();
        leftBucket = new ArrayDeque<>();
        realAns = new ArrayList<>();
        check = 0;
        stackOn = 0;
        for(int i = 0; i<str.length(); i++){
            if(str.charAt(i)=='*'){
                stackOn = 1;
                continue;
            } 

            if(stackOn==1){
                if (str.charAt(i)=='('){
                    check += 1;
                    bucket.add(str.charAt(i));
                } else if (str.charAt(i)==')'){
                    check -= 1;
                    bucket.add(str.charAt(i));
                    if (check == 0){
                        for (char c: bucket){
                            ans.add(c);
                        }
                        if (stackOn== 1)
                            ans.add('*');
                        bucket.clear();
                        stackOn=0;
                    }else{
                        bucket.add(str.charAt(i));
                        continue;
                    }
                } else{
                    if (check == 0){
                        ans.add(str.charAt(i));
                        if (stackOn== 1)
                            ans.add('*');
                        stackOn=0;
                    }else {
                        bucket.add(str.charAt(i));
                    }
                }
            } else{
                ans.add(str.charAt(i));
            }
        }

        bucket.clear();

        StringBuilder sb1 = new StringBuilder();
        for(char c : ans) sb1.append(c);
        String str1= sb1.toString();
        // System.out.println("str1: "+str1);
        ans.clear();
        // System.out.println("ans: "+ans.toString());
        check = 0;
        stackOn = 0;

        for(int i = 0; i<str1.length(); i++){
            if (str1.charAt(i)=='/'){
                stackOn = 2;
                continue;
            }

            if(stackOn==2){
                if (str1.charAt(i)=='('){
                    check +=1;
                    bucket.add(str1.charAt(i));
                } else if (str1.charAt(i)==')'){
                    check -=1;
                    bucket.add(str1.charAt(i));
                    if (check == 0){
                        for (char c: bucket){
                            ans.add(c);
                        }
                        if (stackOn==2)
                            ans.add('/');
                        bucket.clear();
                        stackOn=0;
                    }else {
                        bucket.add(str1.charAt(i));
                        continue;
                    }
                    
                } else{
                    if (check == 0){
                        ans.add(str1.charAt(i));
                        if (stackOn==2)
                            ans.add('/');
                        stackOn=0;
                    }else {
                        bucket.add(str1.charAt(i));
                    }
                }
            } else{
                ans.add(str1.charAt(i));
            }
        }

        stackOn = 0;
        check = 0;

        // System.out.println("ans: "+ans.toString());

        for(int i = 0; i<ans.size(); i++){
            if(ans.get(i)=='+'){
                stackOn = 1;
                continue;
            } else if (ans.get(i)=='-'){
                stackOn = 2;
                continue;
            }

            if(stackOn==1 || stackOn==2){
                if (ans.get(i)=='*'||ans.get(i)=='/'|| ans.get(i)==')'||ans.get(i)=='+'||ans.get(i)=='-'){
                    check = 0;
                    if (ans.get(i)!=')'){
                        bucket.add(ans.get(i));
                    }
                    
                    if(stackOn==1){
                        for(char c : bucket){
                            realAns.add(c);
                        }
                        realAns.add('+');
                        // System.out.println("?? "+ realAns.toString());
                        bucket.clear();
                        stackOn = 0;
                    }
                    else if (stackOn==2){
                        for(char c : bucket){
                           realAns.add(c);
                        }
                        realAns.add('-');
                        bucket.clear();
                        stackOn = 0;
                    }

                    if (ans.get(i)==')'){
                        for(char c : bucket){
                            realAns.add(c);
                        }
                        realAns.add(ans.get(i));
                        
                    }
                    bucket.clear();
                } else {
                    check = 1;
                    bucket.add(ans.get(i));
                    // System.out.println(bucket.toString());
                }
            } else{
                realAns.add(ans.get(i));
                // System.out.println("?? "+ realAns.toString());
            }
        }

        if(!bucket.isEmpty()){
            for(char e : bucket){
                realAns.add(e);
            }
            if (stackOn==1){
                realAns.add('+');
            }else if (stackOn==2){
                realAns.add('-');
            }
            bucket.clear();
        }

        
        StringBuilder sb = new StringBuilder();
        for(char e : realAns){
            if (e!='(' && e!=')'){
                sb.append(e);
            }
        }
        
        System.out.println(sb);
    }

    
}
